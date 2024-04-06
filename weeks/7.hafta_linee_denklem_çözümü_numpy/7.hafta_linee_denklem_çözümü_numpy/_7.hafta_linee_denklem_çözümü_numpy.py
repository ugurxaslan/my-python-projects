import numpy as np

def solve_linear_equation(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        return None

# Örnek kullaným:
A = np.array([[6, 15, 55, 225], [15, 55, 225, 979], [55, 225, 979, 4425], [225, 979, 4425, 20515]])

b = np.array([152.6, 585.6, 2488.8, 11106.0])

x = solve_linear_equation(A, b)

if x is not None:
    print("cozum:")
    print(x)
else:
    print("Denklem sistemi cozulemedi.")

