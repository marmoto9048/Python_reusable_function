from nlgeval import compute_metrics
metrics_dict = compute_metrics(hypothesis='examples/hyp.txt',
                               references=['examples/ref1.txt', 'examples/ref2.txt'])
print('metrics_dict',metrics_dict)