from pprint import pprint

from src.scanner.scanner_engine import ScannerEngine

print("\n========== SCANNER ==========\n")

scanner = ScannerEngine.scan()

pprint(scanner)

print("\n=============================\n")