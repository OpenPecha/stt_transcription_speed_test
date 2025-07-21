# README

> **Note:** This readme template is based on one from the [Good Docs Project](https://thegooddocsproject.dev). You can find it and a guide to filling it out [here](https://gitlab.com/tgdp/templates/-/tree/main/readme). (_Erase this note after filling out the readme._)

<h1 align="center">
  <br>
  <a href="https://openpecha.org"><img src="https://avatars.githubusercontent.com/u/82142807?s=400&u=19e108a15566f3a1449bafb03b8dd706a72aebcd&v=4" alt="OpenPecha" width="150"></a>
  <br>
</h1>

## _Project Name_
_The project name should match its code's capability so that new users can easily understand what it does._

## Owner(s)

_Change to the owner(s) of the new repo. (This template's owners are:)_
- [@ngawangtrinley](https://github.com/ngawangtrinley)
- [@mikkokotila](https://github.com/mikkokotila)
- [@evanyerburgh](https://github.com/evanyerburgh)


## Table of contents
<p align="center">
  <a href="#project-description">Project description</a> •
  <a href="#who-this-project-is-for">Who this project is for</a> •
  <a href="#project-dependencies">Project dependencies</a> •
  <a href="#instructions-for-use">Instructions for use</a> •
  <a href="#contributing-guidelines">Contributing guidelines</a> •
  <a href="#additional-documentation">Additional documentation</a> •
  <a href="#how-to-get-help">How to get help</a> •
  <a href="#terms-of-use">Terms of use</a>
</p>
<hr>

## Project Description
This project aims to measure and compare transcription speed improvements across different transcription methods using a benchmark dataset. The study specifically focuses on the GR (Garchen Rinpoche) catalog, comparing transcription speeds between manual transcription, base STT model-assisted transcription, and fine-tuned model-assisted transcription.

## Objective
To quantitatively assess the difference in transcription rates under three conditions:
1. Pure manual transcription (no reference)
2. Transcription with base STT model reference
3. Transcription with fine-tuned STT model reference

## Methodology

### 1. Benchmark Dataset Selection
- Using unseen data to eliminate model bias
- Dataset comprises 38 original audio IDs
- Each audio file is segmented into multiple parts

### 2. Character Length Analysis
1. Initial Analysis:
   - Calculate character length statistics for each audio segment
   - Group segments by their original audio ID
   - Generate character length distribution report for each original audio

2. Filtering Criteria:
   - Select segments with character length ≥ 30 characters
   - Focus on character length groups with 3 or more instances
   - Rationale: Longer segments better demonstrate transcription speed differences

### 3. Data Distribution Strategy
1. Grouping:
   - Group audio segments by character length ranges (bins)
   - Ensure each group has at least 3 segments
   - Segments are from the same original audio ID

2. Distribution Rules:
   - One segment from each group goes to each CSV file
   - All segments in the same row number across CSVs have similar character length
   - Segments in same row are from same original audio ID but different parts

### 4. Test Design Considerations

1. Audio Source Control:
   - Same row across CSVs uses segments from same original audio
   - Prevents quality/environment variations affecting results
   - Different segments prevent memorization bias

2. Character Length Balance:
   - Similar total character length across all three CSVs
   - Achieved through equal distribution within character length bins

3. Test Files Structure:
   - **File 1 (Manual)**: Audio only, no transcript
   - **File 2 (Base Model)**: Audio + base model transcript
   - **File 3 (Fine-tuned)**: Audio + fine-tuned model transcript

## Test Execution

### For Each CSV File:
1. **Manual Transcription (CSV 1)**
   - Transcriber listens to audio
   - Creates transcript from scratch
   - Time recorded from audio start to transcription completion

2. **Base Model Reference (CSV 2)**
   - Transcriber listens to audio
   - Edits provided base model transcript
   - Time recorded for complete edit process

3. **Fine-tuned Model Reference (CSV 3)**
   - Transcriber listens to audio
   - Edits provided fine-tuned model transcript
   - Time recorded for complete edit process

## Analysis Metrics

1. Time Comparison:
   - Total time taken for each method
   - Speed improvement percentages
   - Average time per character

2. Quality Control:
   - Character length consistency across files
   - Audio source consistency within rows
   - Segment distribution fairness

## Expected Outcomes

- Quantitative comparison of transcription speeds
- Statistical evidence of efficiency improvements
- Documentation of time savings across methods
- Insights into optimal transcription workflow

## Workflow Steps

### 1. Character Length Analysis
```bash
jupyter notebook create_stt_stats.ipynb
```
This notebook:
- Analyzes audio segment character lengths
- Groups segments by original audio ID
- Generates detailed character length distribution report
- Identifies segments meeting test criteria:
  * Character length ≥ 30
  * Groups with 3+ similar length segments
  * Same original audio ID

### 2. Filter Test Data
Using the analysis from `create_stt_stats.ipynb`:
- Filter out segments that don't meet criteria
- Group remaining segments by:
  * Original audio ID
  * Character length range
- Ensure each group has at least 3 segments

### 3. Distribute Data
```bash
python create_csv.py
```
This script:
- Takes filtered segments from analysis
- Distributes them evenly across three CSV files
- Ensures:
  * Same row numbers have similar character lengths
  * Segments in same row are from same original audio
  * No segment repetition across files

    _Explanatory text here_ 
    
    _(Optional: Include a code sample or screenshot that helps your users complete this step.)_

2. _Write the step here._
 
    a. _Substep 1_ 
    
    b. _Substep 2_


### Configure _Project Name_
1. _Write the step here._
2. _Write the step here._


### Run _Project Name_
1. _Write the step here._
2. _Write the step here._


### Troubleshoot _Project Name_
1. _Write the step here._
2. _Write the step here._

<table>
  <tr>
   <td>
    Issue
   </td>
   <td>
    Solution
   </td>
  </tr>
  <tr>
   <td>
    _Describe the issue here_
   </td>
   <td>
    _Write solution here_
   </td>
  </tr>
  <tr>
   <td>
    _Describe the issue here_
   </td>
   <td>
    _Write solution here_
   </td>
  </tr>
  <tr>
   <td>
    _Describe the issue here_
   </td>
   <td>
    _Write solution here_
   </td>
  </tr>
</table>


Other troubleshooting supports:
* _Link to FAQs_
* _Link to runbooks_
* _Link to other relevant support information_


## Contributing guidelines
If you'd like to help out, check out our [contributing guidelines](/CONTRIBUTING.md).


## Additional documentation
_Include links and brief descriptions to additional documentation._

For more information:
* [Reference link 1](#)
* [Reference link 2](#)
* [Reference link 3](#)


## How to get help
* File an issue.
* Email us at openpecha[at]gmail.com.
* Join our [discord](https://discord.com/invite/7GFpPFSTeA).


## Terms of use
_Project Name_ is licensed under the [MIT License](/LICENSE.md).
