"""
Script to load demo data from SQL dump into Django SQLite database
Run this from the project root: python load_demo_data.py
"""
import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from principale.models import Client, Logement, Reservation, ImageLogement

def parse_insert_values(sql_line):
    """Extract values from INSERT statement"""
    # Match VALUES(...) pattern
    match = re.search(r'VALUES\s*\((.*)\)', sql_line, re.DOTALL)
    if not match:
        return []
    
    values_str = match.group(1)
    # Split by comma, but be careful about strings containing commas
    values = []
    current = ""
    in_string = False
    quote_char = None
    
    for char in values_str:
        if char in ("'", '"') and (not in_string or quote_char == char):
            in_string = not in_string
            quote_char = char if in_string else None
            current += char
        elif char == ',' and not in_string:
            values.append(current.strip())
            current = ""
        else:
            current += char
    
    if current.strip():
        values.append(current.strip())
    
    return values

def clean_value(value):
    """Clean SQL value to Python value"""
    value = value.strip()
    if value == 'NULL':
        return None
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.lower() in ('true', '1'):
        return True
    if value.lower() in ('false', '0'):
        return False
    try:
        if '.' in value:
            return float(value)
        return int(value)
    except:
        return value

def load_data():
    """Load demo data from SQL file"""
    with open('demo_data.sql', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Load Users
    print("Loading users...")
    user_inserts = re.findall(
        r"INSERT INTO `auth_user`.*?VALUES\s*\((.*?)\);",
        content,
        re.DOTALL
    )
    for insert in user_inserts:
        # Split by ),( for multiple rows
        rows = re.findall(r'\((.*?)\)(?:,\(|;)', insert)
        for row in rows:
            values = parse_insert_values(f"({row})")
            if len(values) >= 8:
                try:
                    user_id = int(clean_value(values[0]))
                    password = clean_value(values[1])
                    is_superuser = bool(int(clean_value(values[3])))
                    username = clean_value(values[4])
                    is_staff = bool(int(clean_value(values[8])))
                    is_active = bool(int(clean_value(values[9])))
                    email = clean_value(values[7])
                    
                    if not User.objects.filter(username=username).exists():
                        User.objects.create_user(
                            id=user_id,
                            username=username,
                            email=email,
                            password=password,
                            is_staff=is_staff,
                            is_superuser=is_superuser,
                            is_active=is_active
                        )
                        print(f"  ✓ User created: {username}")
                except Exception as e:
                    print(f"  ✗ Error loading user: {e}")
    
    # Load Clients
    print("\nLoading clients...")
    client_inserts = re.findall(
        r"INSERT INTO `principale_client`.*?VALUES\s*\((.*?)\);",
        content,
        re.DOTALL
    )
    for insert in client_inserts:
        rows = re.findall(r'\((.*?)\)(?:,\(|;)', insert)
        for row in rows:
            values = parse_insert_values(f"({row})")
            if len(values) >= 4:
                try:
                    client_id = int(clean_value(values[0]))
                    nom = clean_value(values[1])
                    email = clean_value(values[2])
                    telephone = clean_value(values[3])
                    
                    if not Client.objects.filter(id=client_id).exists():
                        Client.objects.create(
                            id=client_id,
                            nom=nom,
                            email=email,
                            telephone=telephone
                        )
                        print(f"  ✓ Client created: {nom}")
                except Exception as e:
                    print(f"  ✗ Error loading client: {e}")
    
    # Load Logements
    print("\nLoading logements...")
    logement_inserts = re.findall(
        r"INSERT INTO `principale_logement`.*?VALUES\s*\((.*?)\);",
        content,
        re.DOTALL
    )
    for insert in logement_inserts:
        rows = re.findall(r'\((.*?)\)(?:,\(|;)', insert)
        for row in rows:
            values = parse_insert_values(f"({row})")
            if len(values) >= 7:
                try:
                    logement_id = int(clean_value(values[0]))
                    titre = clean_value(values[1])
                    description = clean_value(values[2])
                    adresse = clean_value(values[3])
                    ville = clean_value(values[4])
                    prix_par_nuit = float(clean_value(values[5]))
                    disponible = bool(int(clean_value(values[6])))
                    
                    if not Logement.objects.filter(id=logement_id).exists():
                        Logement.objects.create(
                            id=logement_id,
                            titre=titre,
                            description=description,
                            adresse=adresse,
                            ville=ville,
                            prix_par_nuit=prix_par_nuit,
                            disponible=disponible
                        )
                        print(f"  ✓ Logement created: {titre}")
                except Exception as e:
                    print(f"  ✗ Error loading logement: {e}")
    
    # Load ImageLogements
    print("\nLoading images...")
    image_inserts = re.findall(
        r"INSERT INTO `principale_imagelogement`.*?VALUES\s*\((.*?)\);",
        content,
        re.DOTALL
    )
    for insert in image_inserts:
        rows = re.findall(r'\((.*?)\)(?:,\(|;)', insert)
        for row in rows:
            values = parse_insert_values(f"({row})")
            if len(values) >= 4:
                try:
                    image_id = int(clean_value(values[0]))
                    image = clean_value(values[1])
                    logement_id = int(clean_value(values[2]))
                    description = clean_value(values[3])
                    
                    if not ImageLogement.objects.filter(id=image_id).exists():
                        logement = Logement.objects.get(id=logement_id)
                        ImageLogement.objects.create(
                            id=image_id,
                            image=image,
                            logement=logement,
                            description=description
                        )
                        print(f"  ✓ Image created for logement {logement_id}")
                except Exception as e:
                    print(f"  ✗ Error loading image: {e}")
    
    # Load Reservations
    print("\nLoading reservations...")
    reservation_inserts = re.findall(
        r"INSERT INTO `principale_reservation`.*?VALUES\s*\((.*?)\);",
        content,
        re.DOTALL
    )
    for insert in reservation_inserts:
        rows = re.findall(r'\((.*?)\)(?:,\(|;)', insert)
        for row in rows:
            values = parse_insert_values(f"({row})")
            if len(values) >= 7:
                try:
                    reservation_id = int(clean_value(values[0]))
                    date_arrivee = clean_value(values[1])
                    date_depart = clean_value(values[2])
                    statut = clean_value(values[3])
                    montant_total = float(clean_value(values[4])) if clean_value(values[4]) else None
                    client_id = int(clean_value(values[5]))
                    logement_id = int(clean_value(values[6]))
                    
                    if not Reservation.objects.filter(id=reservation_id).exists():
                        client = Client.objects.get(id=client_id)
                        logement = Logement.objects.get(id=logement_id)
                        Reservation.objects.create(
                            id=reservation_id,
                            date_arrivee=date_arrivee,
                            date_depart=date_depart,
                            statut=statut,
                            montant_total=montant_total,
                            client=client,
                            logement=logement
                        )
                        print(f"  ✓ Reservation created: {client.nom} - {logement.titre}")
                except Exception as e:
                    print(f"  ✗ Error loading reservation: {e}")
    
    print("\n✅ Data loading completed!")

if __name__ == '__main__':
    load_data()
