# Bioinfomatics_Practice_RNAseq
Works for classroom: Bioinfomatics &amp; practice 01 in Seoul Nat'l Univ. 

  ## Content 1: Sars-Cov2 Alignment
  * 2023-04-10 
  > A
  
  > A
  
  ## Content 2: DEG Analysis
    * 2023-05-08
  > Differential gene expression of leishmaniasis

  > RNA seq 데이터를 바탕으로 transcriptomic profiling으로 다양한 형태의 DEG분석을 실습한다. 
    <p align="left">
   </p>
  1. TMP 계산 및 scatter plot
    <p align="left">
   </p>
  2. TMP correlation 확인 (정상 vs leishmania군 구별)
    <p align="left">
   </p>
  3. TMP상의 문제점 확인 : 1) 유전자 길이로 보정해서 짧은 read결과에서 편향 발생(<->RPKM)
                           2) 다른 샘플과의 비교가 부적절
      <p align="left">
  <img src="https://github.com/WoobeenJeong/bioinfo1_jwb/assets/132027211/d7a9dc9c-d5ce-4697-a9bb-2a4b80a15288" alt="image" width="auto" height="100">
   </p>
  4. MA plot 으로 두 그룹(조건) 비교, 이상치 확인
  5. TMM 방식으로 분포 차이나는 두 그룹의 발현량을 가중치로 정규화
      <p align="left">
  <img src="https://github.com/WoobeenJeong/bioinfo1_jwb/assets/132027211/8d079af5-5b32-4ea7-a821-160a44547082" alt="image" width="auto" height="100">
   </p>
  6. PCA analysis
      <p align="left">
  <img src="https://github.com/WoobeenJeong/bioinfo1_jwb/assets/132027211/ec0e0f89-1106-4cb1-b785-594141cfde2c" alt="image" width="auto" height="100">
   </p>
  7. Volcano plot : 발현량 Fold change와 p-value를 바탕으로 타겟 선정
      <p align="left">
  <img src="https://github.com/WoobeenJeong/bioinfo1_jwb/assets/132027211/2bae2935-d3e5-4256-bca2-3fcdb5959f72" alt="image" width="auto" height="100">
   </p>
  8. Heatmap으로 발현의 up/down reg.이 두 비교집단에서 다른 것을 확인
      <p align="left">
  <img src="https://github.com/WoobeenJeong/bioinfo1_jwb/assets/132027211/b2edd6fe-8a33-441e-b7bd-33d0a6ed7a36" alt="image" width="auto" height="100">
   </p>
  10. DAVID에서 타겟의 정보 확인
  
  [> CODE for content 3:](https://github.com/WoobeenJeong/bioinfo1_jwb/blob/main/geneexpr.ipynb)
  [file name] geneexpr.ipynb
  
  
  ## Content 3: EM, Expectation Maximization Algorithm (commonly used tool for Motif study) 
  * 2023-05-15
  > A
  
  > A
  
