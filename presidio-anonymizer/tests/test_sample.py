import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

@pytest.mark.parametrize(
    # fmt: off
        "text, start, end, expText, expStart, expEnd, expLen",
    [
        ("My name is Bond", 11, 15, "My name is BIP", 11, 14, 1
        )    
    ],
    # fmt: on
    )
def test_sample_run_anonymizer(text, start, end, expText, expStart, expEnd, expLen):
    result = sample_run_anonymizer(text, start, end)
    assert result.text== expText
    assert result.items[0].start== expStart
    assert result.items[0].end== expEnd
    assert len(result.items)== expLen