import numpy as np

class TemperatureMonitor:
    def __init__(self, lower_limit=20.0, upper_limit=80.0):
        self.temperatures = []
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        print(f"Monitor inicializado. Limites de segurança: {lower_limit}°C a {upper_limit}°C.")

    def add_reading(self, temperature):
        self.temperatures.append(temperature)
        print(f"Nova leitura adicionada: {temperature}°C.")
        
        if not self.is_within_safe_limits(temperature):
            print(f"ALERTA DE SEGURANÇA! Temperatura {temperature}°C fora dos limites ({self.lower_limit}°C - {self.upper_limit}°C).")

    def is_within_safe_limits(self, temperature):
        return self.lower_limit <= temperature <= self.upper_limit

    def calculate_statistics(self):
        if not self.temperatures:
            return None, None, None
        
        temps_array = np.array(self.temperatures)
        max_temp = np.max(temps_array)
        min_temp = np.min(temps_array)
        mean_temp = np.mean(temps_array)
        
        return max_temp, min_temp, mean_temp

    def display_statistics(self):
        max_temp, min_temp, mean_temp = self.calculate_statistics()
        
        print("\nRELATÓRIO DE MONITORAMENTO ESTATÍSTICO")
        print("---------------------------------------")
        
        if max_temp is None:
            print("Nenhuma leitura de temperatura registrada para calcular estatísticas.")
        else:
            print(f"Máxima Registrada: {max_temp:.2f}°C")
            print(f"Mínima Registrada: {min_temp:.2f}°C")
            print(f"Média das Leituras: {mean_temp:.2f}°C")
            print("---------------------------------------")
            print(f"Limites de Segurança: {self.lower_limit}°C a {self.upper_limit}°C.")

if __name__ == "__main__":
    monitor = TemperatureMonitor()
    print("\n--- INÍCIO DA DEMONSTRAÇÃO (LEITURAS SEGURAS) ---")
    
    leituras_seguras = [35.5, 55.0, 79.9]
    for temp in leituras_seguras:
        monitor.add_reading(temp)

    print("\n--- LEITURAS COM ALERTA ---")

    leituras_alerta = [15.2, 95.0, 60.0]
    for temp in leituras_alerta:
        monitor.add_reading(temp)

    monitor.display_statistics()

    monitor_custom = TemperatureMonitor(lower_limit=5.0, upper_limit=10.0)
    print("\n--- DEMONSTRAÇÃO DE LIMITES CUSTOMIZADOS (5°C - 10°C) ---")
    monitor_custom.add_reading(8.5)
    monitor_custom.add_reading(12.0)

    monitor_custom.display_statistics()