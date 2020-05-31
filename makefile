BTC_PRICE_SCRIPT = btc_price.py
BTC_FEES_SCRIPT = btc_fees.py
BTC_PRICE = btc_price
BTC_FEES = btc_fees

.PHONY: install clean

install: btc_price.py btc_fees.py
	@cp ${BTC_PRICE_SCRIPT} ~/.local/bin/${BTC_PRICE}
	@chmod +x ~/.local/bin/${BTC_PRICE}
	@cp ${BTC_FEES_SCRIPT} ~/.local/bin/${BTC_FEES}
	@chmod +x ~/.local/bin/${BTC_FEES}
	@echo "Copied scripts to ~/.local/bin, and set as executable."

clean:
	@rm ~/.local/bin/${BTC_PRICE}
	@rm ~/.local/bin/${BTC_FEES}
	@echo "Removed ${BTC_PRICE} and ${BTC_FEES} from ~/.local/bin/"
