# Evaluating STT Model-Assisted Transcription Speed: A Case Study with Garchen Rinpoche's Teachings

## Introduction
In the realm of Tibetan Buddhist teachings preservation, transcription of oral teachings plays a crucial role. We conducted a comprehensive study to evaluate whether Speech-to-Text (STT) models could significantly improve transcription speed. Our study focused on Garchen Rinpoche's teachings, comparing three transcription methods: manual transcription, base STT model-assisted transcription, and fine-tuned model-assisted transcription. While our initial hypothesis suggested that both STT-assisted methods would consistently improve transcription speed, our findings revealed a more nuanced reality.

## Background
Traditional manual transcription of Buddhist teachings is time-consuming and resource-intensive. Modern STT technology promises to streamline this process, but its effectiveness in real-world scenarios needed validation. We hypothesized that providing transcribers with machine-generated transcripts would significantly reduce transcription time, with fine-tuned models offering superior performance over base models.

## Methodology

### Dataset Preparation and Standardization

#### 1. Initial Selection and Filtering
- Selected segments from Garchen Rinpoche's Benchmark
- Carefully filtered for segments ≥30 characters
- Grouped by original audio ID and character length

#### 2. Strategic Distribution Design

**a. Character Length Standardization**
- Segments in corresponding rows across all three test sets have similar character lengths
- **Why This Matters**: 
  * Ensures fair comparison of transcription speeds
  * Longer segments might naturally take more time to transcribe
  * Similar character lengths provide a standardized basis for measuring speed improvements
  * Eliminates bias from varying text complexity

**b. Audio Source Management**
- Different segments from the same original audio used across test conditions
- **Why This Matters**:
  * Prevents transcriber memorization bias
  * If same segment appeared in multiple tests, transcribers might remember content
  * Memory advantage would artificially improve transcription speed
  * Using different segments ensures genuine speed measurement

**c. Distribution Balance**
- Similar total character counts across all three test sets
- Equal representation of audio sources
- **Why This Matters**:
  * Maintains consistent workload across all three conditions
  * Ensures fair comparison between manual, base, and fine-tuned approaches
  * Controls for variations in audio quality and speaker patterns

### Test Design
1. **Manual Transcription**: No reference transcript provided
2. **Base Model Assisted**: Base STT model transcript provided
3. **Fine-tuned Model Assisted**: Fine-tuned model transcript provided

### Test Execution
- Four experienced transcribers participated
- Three transcribers processed 25 segments per method one transcriber 18 segments per method due to lack of test data.
- Time measurements captured using specialized Google Sheets script
- Character counts and accuracy metrics recorded

## Results

### Key Metrics Visualization

```
Transcription Speed (characters/minute)

Manual:     47.86 ┤████████████████████
Base:       49.85 ┤█████████████████████
Fine-tuned: 77.67 ┤████████████████████████████████

Total Time Savings vs Manual (minutes)

Base:       3.52  ┤█
Fine-tuned: 40.60 ┤████████████████

Speed Improvement Percentage

Base:       3.31%  ┤█
Fine-tuned: 38.25% ┤███████████████
```

### Individual Transcriber Performance

#### Speed Metrics by Transcriber

| Transcriber | Manual (chars/min) | Base Model (chars/min) | Fine-tuned (chars/min) |
|------------|-------------------|----------------------|----------------------|
| Transcriber 1 | 55.40 | 54.69 (-6.64%) | 94.57 (+34.42%) |
| Transcriber 2 | 37.70 | 42.27 (+35.69%) | 57.79 (+47.11%) |
| Transcriber 3 | 78.63 | 69.87 (-18.02%) | 183.56 (+45.44%) |
| Transcriber 4 | 56.99 | 56.47 (-36.20%) | 73.92 (+12.73%) |

*Note: Percentages in parentheses show speed improvement vs manual transcription. Negative values indicate slower performance.*

### Overall Performance (Across All Transcribers)

| Metric | Manual | Base Model | Fine-tuned Model |
|--------|---------|------------|------------------|
| Total Time (minutes) | 106.15 | 102.63 | 65.55 |
| Total Characters | 5,080 | 5,116 | 5,091 |
| Segments Count | 93 | 93 | 93 |
| Average Speed (chars/min) | 47.86 | 49.85 | 77.67 |
| Time Saved vs Manual (min) | - | 3.52 | 40.60 |
| Speed Improvement | - | 3.31% | 38.25% |

### Individual Transcriber Variations

#### Key Findings
1. **Most Significant Improvements**:
   - Transcriber 2 showed the highest improvement with fine-tuned model (+47.11%)*
   - Also uniquely improved with base model (+35.69%)
   - Notable progression from slowest manual speed (37.70 chars/min) to significant improvements with both models
   - *Note: Based on 18 segments per method, while others completed 25 segments

2. **Base Model Performance Variance**:
   - Three out of four transcribers were slower with base model
   - Most severe slowdown: Transcriber 4 (-36.20%)
   - Only Transcriber 2 showed positive improvement

3. **Fine-tuned Model Consistency**:
   - All transcribers improved with fine-tuned model
   - Improvements ranged from 12.73% to 47.11%
   - Even the lowest improvement (Transcriber 4: +12.73%) was significant
   - Transcriber 3 achieved second-highest improvement (45.44%) with full 25-segment set

## Analysis of Individual Performance Patterns

### Transcriber Experience Patterns
1. **High Performers with Fine-tuned Model**
   - Transcribers 2 and 3 showed exceptional improvement (>45%)
   - Suggests optimal adaptation to assisted transcription workflow

2. **Base Model Challenges**
   - Three out of four transcribers were slower with base model
   - Most significant slowdown: Transcriber 4 (-36.20%)
   - Only Transcriber 2 showed improvement with base model

3. **Consistency Patterns**
   - All transcribers improved with fine-tuned model
   - Improvement range varied significantly (12.73% to 47.11%)
   - Suggests individual adaptation differences

## Discussion

### The Base Model Paradox
Our most surprising finding was that base model assistance sometimes increased transcription time. This could be attributed to:
1. Lack of domain-specific training
   - Base model not specifically fine-tuned for Garchen Rinpoche's audio
   - Higher error rate with Buddhist terminology and teaching context
   - Editing errors often more time-consuming than fresh transcription

2. Mental Context Switching
   - Transcribers must constantly switch between listening and comparing with base model output
   - Additional effort required to identify and correct errors while maintaining context
   - Fresh transcription allows more natural flow of listening and typing

3. Trust and Verification Issues
   - Low confidence in base model leads to double-checking every word
   - Transcribers spend extra time verifying even correct transcriptions
   - Psychological barrier: knowing it's a general model makes transcribers more skeptical

### Fine-tuned Model Success
The consistent improvement with fine-tuned model assistance across all transcribers validates the value of domain-specific model training. Key factors contributing to success:
1. Higher accuracy reducing verification time
2. Better handling of domain-specific terminology
3. Increased transcriber confidence in machine output

## Conclusions and Recommendations

1. **Fine-tuned Models**: Strongly recommended for transcription assistance, showing consistent speed improvements (12-45%)

2. **Base Models**: Use with caution
   - May not always improve efficiency
   - Consider transcriber-specific workflows
   - May require additional training for effective use

3. **Future Considerations**:
   - Develop transcriber training for optimal use of STT assistance
   - Further investigate why base models sometimes reduce efficiency
   - Consider transcriber-specific customization of workflows

## Resources and Data Access

### Test Results and Analysis
- Complete test results and analysis are available in our [Google Drive folder](https://drive.google.com/drive/folders/12TYEOWcc5vsTFl7TLUgYdpRm8avn6eNF)
- Includes detailed transcription timing data and comparative analysis across methods

### Source Code
- GitHub Repository: [OpenPecha/stt_transcription_speed_test](https://github.com/OpenPecha/stt_transcription_speed_test/tree/transcribing_speed_test)
- Contains scripts for:
  * Test data creation and distribution
  * Results analysis
  * Statistical computations

## Acknowledgments
Special thanks to our four transcribers who participated in this study.

---
*This research was conducted as part of the OpenPecha initiative to improve the preservation and accessibility of Buddhist teachings.*
