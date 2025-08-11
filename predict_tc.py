# КАЛЬКУЛЯТОР Tc
def calculate_tc(dimensionality, ion_complexity, defect_density):
    """
    ФОРМУЛА: T_c = T0 * sqrt(C_max / C_lattice)
    Где C_lattice = 10000 * ion_complexity * (0.7 если 2D) * (1 + 2*defect_density)
    """
    T0 = 95.0  # Для купратов
    C_max = 1800000
    
    # Расчёт сложности решётки
    base_complexity = 10000 * ion_complexity
    dim_factor = 0.7 if dimensionality == 2 else 1.0
    defect_factor = 1 + 2 * defect_density
    C_lattice = base_complexity * dim_factor * defect_factor
    
    if C_lattice > C_max:
        return 0  # Нет сверхпроводимости
    else:
        return round(T0 * (C_max / C_lattice)**0.5, 1)

# Пример использования:
print("Предсказанная Tc для YBCO:", calculate_tc(2, 4.2, 0.1), "K")
