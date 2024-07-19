from calculadora import Calculadora

def main():
    """
    Main function to start the calculator application.
    """
    try:
        calculadora = Calculadora()        
        calculadora.mainloop()
        
    except ImportError as e:
        print(f"Error importing the Calculadora class: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
