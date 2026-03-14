import random

class RyanairSeatingSim:
    def __init__(self):
        # Rows 1 to 33, Seats A-F
        self.rows = range(1, 34)
        self.cols = ['A', 'B', 'C', 'D', 'E', 'F']
        self.seats = {}
        self.initialize_seats()

    def initialize_seats(self):
        for r in self.rows:
            for c in self.cols:
                # Row 1 only has ABC
                if r == 1 and c in ['D', 'E', 'F']:
                    continue
                
                seat_id = f"{r}{c}"
                score = self.calculate_score(r, c)
                self.seats[seat_id] = {
                    'score': score,
                    'status': 'AVAILABLE' # AVAILABLE, LOCKED, OCCUPIED
                }

    def calculate_score(self, row, col):
        score = 50 # Base score

        # Premium Rows (Front and Exit)
        if row == 1: score += 40
        if row in [16, 17]: score += 35
        if row in [2, 3, 4, 5]: score += 20
        
        # Last rows are bad
        if row >= 30: score -= 20
        
        # Position score
        if col in ['A', 'F']: score += 10 # Window
        if col in ['C', 'D']: score += 5  # Aisle
        if col in ['B', 'E']: score -= 15 # Middle
        
        # Missing windows (typical in 737)
        if (row == 11 and col == 'A') or (row == 12 and col in ['A', 'F']):
            score -= 10
            
        return score

    def get_worst_available_seats(self, count):
        available = [s for s, data in self.seats.items() if data['status'] == 'AVAILABLE']
        # Sort by score ascending (worst first)
        available.sort(key=lambda s: self.seats[s]['score'])
        return available[:count]

    def assign_seat_automatically(self, passenger_name):
        # Ryanair's greedy algorithm: pick the worst available seat
        worst_seats = self.get_worst_available_seats(1)
        if not worst_seats:
            return None
        
        seat_id = worst_seats[0]
        self.seats[seat_id]['status'] = 'OCCUPIED'
        self.seats[seat_id]['passenger'] = passenger_name
        return seat_id

    def lock_seats(self, seat_ids):
        for sid in seat_ids:
            if self.seats[sid]['status'] == 'AVAILABLE':
                self.seats[sid]['status'] = 'LOCKED'

    def unlock_seats(self, seat_ids):
        for sid in seat_ids:
            if self.seats[sid]['status'] == 'LOCKED':
                self.seats[sid]['status'] = 'AVAILABLE'

    def print_status(self):
        print("\n--- Estado del Avión ---")
        occupied_count = sum(1 for s in self.seats.values() if s['status'] == 'OCCUPIED')
        locked_count = sum(1 for s in self.seats.values() if s['status'] == 'LOCKED')
        available_count = sum(1 for s in self.seats.values() if s['status'] == 'AVAILABLE')
        print(f"Ocupados: {occupied_count} | Bloqueados: {locked_count} | Libres: {available_count}\n")

def run_simulation():
    sim = RyanairSeatingSim()
    
    # 1. Simular 100 pasajeros haciendo check-in normal (gratis)
    print("Simulando 100 check-ins automáticos iniciales (pasajeros estándar)...")
    for i in range(100):
        sim.assign_seat_automatically(f"Pax_{i}")
    
    sim.print_status()
    
    # 2. El "Ataque": Bloqueamos los 30 peores asientos disponibles
    print("[!] EJECUTANDO EXPLOIT: Bloqueando los 30 peores asientos para 'limpiar' el pool...")
    worst_30 = sim.get_worst_available_seats(30)
    sim.lock_seats(worst_30)
    
    sim.print_status()
    
    # 3. Nuestro check-in
    print(">>> Realizando TU check-in ahora...")
    tu_asiento = sim.assign_seat_automatically("TU (The Engineer)")
    
    if tu_asiento:
        seat_data = sim.seats[tu_asiento]
        print(f"\nRESULTADO: Te han asignado el asiento {tu_asiento} (Score de calidad: {seat_data['score']})")
        if seat_data['score'] > 60:
            print("ÉXITO: El sistema se vió obligado a darte un asiento Premium.")
        else:
            print("El pool era demasiado grande; se necesitan más bloqueos para llegar a los Premium.")
    
    # 4. Liberar bloqueos
    sim.unlock_seats(worst_30)
    print("\n[+] Bloqueos temporales liberados (sesiones expiradas).")

if __name__ == "__main__":
    run_simulation()
