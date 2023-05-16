pwd
ls 
whoami

conda activate base
mamba activate lab
samtools

mkdir covprj1
cd covprj1/

### NCBI SRA : search "egypt/nrc-01" 
### SRX = experitment is culmulated / SRR = only once data 
### SRR11667146 read length is noticible
### in illumia, read +1 for correction, but not neccesary now
### data access -> download 

curl -o NRC-01.fastq.gz https://sra-pub-sars-cov2.s3.amazonaws.com/sra-src/SRR11667146/NRC-01_S13_L001_R1_001.fastq.gz

md5sum NRC-01.fastq.gz 
gunzip NRC-01.fastq.gz 
ls -al

#### u can use arrow key up down, and q to quit
less NRC-01.fastq

mkdir sequences
mv NRC-01.fastq sequences/

# can see from middle of the file, unzip can be done
bgzip sequences/NRC-01.fastq 

zless sequences/NRC-01.fastq.gz
ls -al sequences/

### NCBI ReFseq https://www.ncbi.nlm.nih.gov/nuccore/1798174254
### search: SARS COV2
### FASTA click
### CoV.fa save the file in covprj1

### or, send to -> click file -> fasta get and drag-drop to VScode
### move it to file mkdir "reference"

### indexing, option -a for small reference
bwa
bwa index
bwa index -a is reference/CoV.fa 

### can see option, in illumina no need to, except alot of mutation or jumping RNA
bwa mem
bwa mem reference/CoV.fa sequences/NRC-01.fasta.gz | less

### number1 S number2 M = number1=waste, number=match

### copy for misterious seq
### make seqinv.ipynb
### select kernel
seq = """
TAACAAAGCCTTACATTAAGTGGGATTTGTTAAAATATGACTTCACGGAAGAGCTGTCTCTTATACACATCTCCGAGCCCACGAGACTAAGGCGAATCTCGTATGCCGTCTTCTGCTTGAAAAAAAATTCTCTTCTTTTTTTCTTTTTCTCTTTTTTTTTCTTTTTTTTTTTCTTTTTCTTTTTTTTTTTTTTTCTCTTTCTCTTTCTTCCTTTCTCTCTTCTTTTTTCTTTTTTTTTCTTCTCTTCTTTT
""".strip().replace('\n', '')

len(seq)

seq[53:]

### in less, you can find seq by /ATTTATATA
### adaptor trimming = leftover became an adaptor, so that we need to trim it
### we have to cut both size
pip install cutadap
cutadapt -a CTGTCTTTATACACATCT -m 30 sequences/NRC-01.fastq.gz | less
cutadapt -a CTGTCTTTATACACATCT -m 30 sequences/NRC-01.fastq.gz > sequences/clipped-NRC01.fastq

nproc --all
bgzip -@ 16 sequences/clipped-NRC01.fasta

bwa mem reference/CoV.fa sequences/clipped-NRC01.fastq.gz > NRC-01.sam

### NC_045512.2	14222 <- this is location of genome, that are not stll sorted on sam file
### sam is text format, so in meta data -> need to zip

mkdir alignments
mv NRC-01.sam alignments/

samtools view -b -o alignments/NRC-01.bam alignments/NRC-01.sam 
samtools sort -o alignments/NRC-01.sorted.bam alignments/NRC-01.bam 
samtools index alignments/NRC-01.sorted.bam 
### but too many disc needed
bwa mem reference/CoV.fa sequences/clipped-NRC01.fastq.gz | samtools sort -o alignments/NRC-01.sorted.bam alignments/NRC-01.sorted2.bam

### download bam & bam.bai
### igv.org -> web app -> Genome : choose Sars-Cov2  /  put Tracks : bam & bam.bai together
### coverage track = like mountain there is higher point = that higher coverage

### https://genome.ucsc.edu/ -> Genomes -> Sars cov2 -> pack -> nextstrainClade.bb download  
### covprj1 <- mv nextstrainClade.bb (by drag to workspace)

mamba install -y ucsc-bigbedtobed ucsc-bedtobigbed
bigBedToBed nextstrainClade.bb nextstrainClade.bed
sed -e 's/NC_045512v2/NC_045512.2/g' nextstrainClade.bed > nextstrainClade-igv.bed

echo "NC_045512.2 29903" > chrom.sizes
bedToBigBed -type=bed12+8 -tab nextstrainClade-igv.bed chrom.sizes nextstrainClade-igv.bb

### download file,
### upload on igv, so that you can use location of mutation
### especially track height can be adjusted to see more clearly by clicking the gear icon 

samtools mplieup -f reference/CoV.fa alignments/NRC-01.sorted.bam | less

/14407 # TTtTTTt <- well conducted mutation, also 14408 in above

bcftools mpileup -Ov -f reference/CoV.fa alignments/NRC-01.sorted.bam | less
mkdir variants
bcftools mpileup -Ov -f reference/CoV.fa alignments/NRC-01.sorted.bam > variants/NRC-01.vcf

bcftools call -mv --ploidy 1 -Ob -o variants/NRC-01.bcf variants/NRC-01.vcf 

bcftools view variants/NRC-01.bcf | less
bcftools view variants/NRC-01.bcf > variants/NRC-01.called.vcf
bgzip variants/NRC-01.called.vcf 
bcftools index variants/NRC-01.called.vcf.gz 

### u can download vcf.gz and vcf.gz.csi, putting igv.org and you can see more detail about mutation points

