import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Application started")
    print("Hello World")
    logging.info("Application finished")

if __name__ == "__main__":
    main()
