import warnings
from Bio import BiopythonWarning
warnings.filterwarnings("ignore", category=BiopythonWarning)
from Bio.Seq import Seq
# Take DNA sequence input from user
dna = input("Enter dna sequence:")
# Convert to Biopython Seq object for biological operations
dna_input = Seq(dna)
# Calculate sequence length
print("DNA:", dna) 
length = len(dna) 
print("Length:", length)
# Count individual nucleotide bases
a = dna.count("A")
t = dna.count("T") 
g = dna.count("G")
c = dna.count("C") 
print("A:", a, "T:", t, "G:", g, "C:", c) 
# Validate sequence length
if length > 100:
    print("✅ Valid DNA sequence")
elif 30 <= length < 100:
   print("⚠️ Short sequence — limited analysis")
else:
    print("❌ Too short!")
# Calculate GC% and AT% — indicator of genomic stability
gc = g + c 
at = a + t
gc_percent = (gc / length) * 100
at_percent = (at / length) * 100
print("GC%:", gc_percent) 
#  Normal GC range is 40-60% in most organisms
print("AT%:", at_percent)
if 40 <= gc_percent <= 60:
  print("✅ Normal GC range")
elif 35 <= gc_percent < 40 or 60 < gc_percent <= 65: 
   print("⚠️ Borderline GC% — specific genomic region or unique organism")
else: 
  print("⚠️ Abnormal GC% — possible mutation!")
# Generate complementary strand
print("Complementary strand:" , dna_input.complement())
print("-"*30)
print("Reverse complement:" , dna_input.reverse_complement())
print("-"*30)
# Transcribe DNA to RNA
print("RNA:" , dna_input.transcribe())
print("-"*30)
# Translate RNA to Protein (stops at stop codon)
print("Protein:" , dna_input.translate(to_stop = True))


