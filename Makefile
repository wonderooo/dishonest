DIRS = lcd keyboard
PORT = /dev/cu.usbmodem1401

all: $(DIRS) run

$(DIRS):
	@for file in $@/*; do \
		mpremote connect port:$(PORT) fs cp $$file :$$file; \
	done

run:
	mpremote connect port:$(PORT) run main.py;

.PHONY: all $(DIRS) run