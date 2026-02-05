import sys
import os

vml_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "vml"))
if vml_dir not in sys.path:
    sys.path.insert(0, vml_dir)

try:
    import vml_engine
    print("Importing moduls is successful.")
except ImportError as e:
    print("Failed to import module.")
    sys.exit(1)

def test_vml_logic():
    target_var = 100
    var_name = "target_var"
    
    frame = sys._getframe()
    
    print(f"\n--- Test for Engine: {var_name} ---")

    result = vml_engine.check_variable(frame, 100, var_name, "L")
    print(f"Result: (No Change): {result} -> {'Successful' if result is False else 'Fail'}")

    result = vml_engine.check_variable(frame, 50, var_name, "L")
    print(f"Result: (Changed): {result} -> {'Successful' if result is True else 'Fail'}")

    result = vml_engine.check_variable(frame, 100, "no_such_var", "L")
    print(f"Result: (None): {result} -> {'Successful' if result is None else 'Fail'}")

if __name__ == "__main__":
    test_vml_logic()