from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer():
    
    text=input("text: ")
    start=int(input("start: "))
    end=int(input("end: "))

    result = testable_anonymizer(text, start, end)
    print(result)
    
   

def testable_anonymizer(inText: str, begin: int, stop: int):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=inText,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=begin, end=stop, score=0.8)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

     # input should be:
    # text: My name is Bond.
    # start: 11
    # end: 15
    # 
    # output should be:
    # text: My name is BIP.
    # items:
    # [
    #     {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    # ]

    return result


if __name__ == "__main__": 
    #sample_run_anonymizer();
    text = "My name is Bond."
    start = 11
    end = 15
    result = testable_anonymizer(text, start, end)
    print(result)