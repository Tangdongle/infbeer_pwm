DB=db.db
PYTHON=$(which python3)

build:
	sudo apt install git python3 python3-pip sqlite3 git-core python3-gpiozero
	ssh-keygen -t rsa -f /home/pi/.ssh/id_rsa -q -P ""
	git clone git@github.com:Tangdongle/infbeer_pwm.git
	cd infbeer_pwm
	pip3 install -r requirements.txt
	touch $(DB)
	python3 db.py



