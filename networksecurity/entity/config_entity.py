from datetime import datetime
import os
from networksecurity.constant import training_pipeline

print(training_pipeline.ARTIFACT_DIR)
print(training_pipeline.PIPELINE_NAME)

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m-%d-%Y-%H-%M-%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)