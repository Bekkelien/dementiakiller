# Dementiakiller is a speech recognition application

Approximate 10s Sequence length for speech ATM.


- | It learns something?
- | Bad Prepossess?
- | To simple network, need Conv's and stuff? 
- | BUG's?
- | All data are in the test data (No validation so test data are from train data for now, which really it shouldn't)
- | Padding is now 0 everywhere

To be trained on LJSpeech-1.1 dataset:
[LJSpeech]: https://keithito.com/LJ-Speech-Dataset/

DIP's - Dementiakiller Improvement Proposal 
- [ ] Normalize data?
- [ ] Normalize the encodings?
- [ ] Prepossess is stupid 
- [ ] Does the space in CHARSET set to 0 become a problem with CTC loss, special char how does this work?