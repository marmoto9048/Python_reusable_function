from Read_Save import save
from nlgeval import compute_metrics

metrics_dict = compute_metrics(hypothesis='2-PQG/3-predict-100.txt',references=['2-PQG/3-reference-100.txt'])# #
# input_file_path = "test-100.txt"
print('metrics_dict',metrics_dict)
output_file_path = "2-PQG/results.txt"
save(output_file_path, metrics_dict)










