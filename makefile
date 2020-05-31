install: btc_price.py btc_fees.py
	@cp btc_price.py ~/.local/bin/btc_price
	@chmod +x ~/.local/bin/btc_price
	@cp btc_fees.py ~/.local/bin/btc_fees
	@chmod +x ~/.local/bin/btc_fees
	@echo "Copied scripts to ~/.local/bin, and set as executable."
