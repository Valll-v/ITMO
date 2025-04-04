package Asin;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestInstance.Lifecycle;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import Asin.Asin.*;
import Asin.Exceptions.*;


@TestInstance(Lifecycle.PER_CLASS)
class AsinTest {

	private Asin asin;
	
	@BeforeAll
	public void setUp() {
		this.asin = new Asin();
	}

    @ParameterizedTest
    @CsvSource({
        "0.5, 0.01",
        "-0.5, 0.01",
        "0.7, 0.1",
        "1.0, 0.25",
        "-1.0, 0.25",
        "0.0, 0.0",
    })
    void testOk(double x, double e) throws WrongValueException {
        Assertions.assertTrue(Math.abs(this.asin.asin(x, 10) - Math.asin(x)) <= e);
    }

    @ParameterizedTest
    @ValueSource(doubles = { -2.0, 2.0, 100, 1.001})
    void testException(double x) throws WrongValueException {
        Assertions.assertThrows(WrongValueException.class, () -> this.asin.asin(x, 10));
    }
}
