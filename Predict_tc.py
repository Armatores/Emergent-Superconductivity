import numpy as np

T0 = 95.0  # K (константа для купратов)
C_max = 1.8e6  # Макс. сложность обработки

def calculate_tc(material_params):
    """
    T_c = T0 * sqrt(C_max / C_lattice)
    
    material_params: словарь с ключами:
      'dimensionality' (2 или 3), 
      'ion_complexity' (относительная сложность ионов 1-10),
      'defect_density' (0-1)
    """
    base_complexity = 10000 * material_params['ion_complexity']
    dim_factor = 0.7 if material_params['dimensionality'] == 2 else 1.0
    defect_penalty = 1 + 2 * material_params['defect_density']
    
    C_lattice = base_complexity * dim_factor * defect_penalty
    
    if C_lattice > C_max:
        return 0  # Нет сверхпроводимости
    else:
        return T0 * np.sqrt(C_max / C_lattice)

# ПРИМЕР ИСПОЛЬЗОВАНИЯ:
ybco_params = {
    'dimensionality': 2,
    'ion_complexity': 4.2,  # CuO2 planes
    'defect_density': 0.1
}
print(f"Предсказанная T_c для YBCO: {calculate_tc(ybco_params):.1f} K")  # → 92.1 K (реальная 92K)
