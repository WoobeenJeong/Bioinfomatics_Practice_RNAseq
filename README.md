# Bioinfomatics_Practice_RNAseq
Works for classroom: Bioinfomatics &amp; practice 01 in Seoul Nat'l Univ. 

  # Contents
  **#1. Genome Alignment**
  
  **#2. DEG Analysis**
  
  **#3. EM algo. Motif study**
  
  **#4. GO Analysis & GSEA**
  
  * based on RNAseq data (include Ribo-seq, CLIP-seq)

  ## Lesson 1: Genome Alignment
  * 2023-04-10 
  > Alignment of Sars-Cov2 genome: egypt/nrc-01 and Variant calling
  
  > NCBI SRA 데이터베이스에서 받은 raw data(fasta형식)을 바탕으로 samtools 활용법을 익히고 indexing을 바탕으로하는 alignment와 variant calling을 확인한다. 
  
[>CODE 001](https://github.com/WoobeenJeong/Bioinfomatics_Practice_RNAseq/blob/main/raw_001_Align_Sars_Cov2.py)
  : raw_001_Align_Sars_Cov2.py
  
  ## Lesson 2: DEG Analysis
  * 2023-05-08
  > Differential gene expression of leishmaniasis

  > RNA seq 데이터를 바탕으로 transcriptomic profiling으로 다양한 형태의 DEG분석을 실습한다. 

[>CODE 002](https://github.com/WoobeenJeong/Bioinfomatics_Practice_RNAseq/blob/main/002_DEG_analysis.ipynb)
    : 002_DEG_analysis.ipynb

  
  ## Lesson 3: Expectation Maximization Algorithm  <br/> (as commonly used tool for Motif study) 
  * 2023-05-15
  > Finding motif by commonly used EM algorithm
  
  > 시퀀싱 데이터를 분석하는 다양한 알고리즘에 있어, 다양한 level에서 가장 broad하게 사용되는 Motif finding 알고리즘인 EM 알고리즘의 구성을 이해하고 각각의 프로세스의 의미와 결과가 타당한지 해석한다.
  
   [>CODE 003](https://github.com/WoobeenJeong/Bioinfomatics_Practice_RNAseq/blob/main/003_Motif_EM.ipynb)
  : 003_Motif_EM.ipynb

  
  ## Lesson 4: Gene Ontology analysis and geneset enrichment analysis
  * 2023-05-22
  > Gene function in term and it's abundance on leishmaniasis 
  
  > 기존의 분석과 달리, gene ontology(term)상에서 network 및 pathway analysis를 위한 기능적 발현을 중심으로 정량분석을 진행한다.
  
   [>CODE 004](https://github.com/WoobeenJeong/Bioinfomatics_Practice_RNAseq/blob/main/004_GO_GSEA.ipynb)
  : 004_GO_GSEA.ipynb

