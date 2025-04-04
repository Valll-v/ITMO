package Asin.Asin;

import Asin.Exceptions.WrongValueException;

public class Asin {

    private int factorial(int x) {
    	if (x <= 1) {
    		return 1;
    	}
    	return x * this.factorial(x - 1);
    }

    private double pow(double x, int n) {
    	double result = 1;
    	for (int i = 0; i < n; i++) {
    		result *= x;
    	}
    	return result;
    }

    public double asin(double x, int n) throws WrongValueException {
    	if (x * x > 1) {
    		throw new WrongValueException("Abs sin value cannot be more than 1");
    	}
        double result = 0;
        for (int i = 0; i < n; i++) {
        	double item = 1;
        	long item_1 = this.factorial(2 * i);
        	long item_2 = this.factorial(i) * this.factorial(i);
        	if (item_1 <= 0 || item_2 <= 0) {
        		break;
        	}
        	double item_3 = this.pow(4, i);
        	item *= item_1 / item_2 / item_3;
        	item *= this.pow(x, 2 * i + 1) / (2 * i + 1);
        	result += item;
        }
        return result;
    }
}