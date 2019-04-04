from allennlp.predictors.predictor import Predictor

def comprehend(passage, question):
    predictor = Predictor.from_path("bidaf-model-2017.09.15-charpad.tar.gz")
    return predictor.predict(passage=passage, question=question)
