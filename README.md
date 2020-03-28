# FTL-task
Steps for start python django server and call API
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
cd /opt
wget https://www.python.org/ftp/python/3.5.6/Python-3.5.6.tgz
sudo tar xzf Python-3.5.6.tgz
cd Python-3.5.6
sudo ./configure
sudo make
sudo make install
whereis python
<path-of-python3.5.6> -m venv venv
source venv/bin/activate
In case you want change models(for now this is done. migrations file and db.sqlite3 file pushed on git):
	python manage.py makemigrations
	python manage.py migrate
To populate data:
python manage.py populate_data
nohup python manage.py runserver --noreload &

API DOCUMENTATION:
url: 127.0.0.1:8000/show-data
request type: get/post(any)
Response:
{
  "members": [
    {
      "activity_periods": [
        {
          "end_time": "Mar 28 2020 07:18pm",
          "start_time": "Mar 28 2020 06:48pm"
        },
        {
          "end_time": "Mar 28 2020 07:48pm",
          "start_time": "Mar 28 2020 07:18pm"
        },
        {
          "end_time": "Mar 28 2020 08:18pm",
          "start_time": "Mar 28 2020 07:48pm"
        }
      ],
      "id": 1,
      "real_name": "Egon Spengler",
      "tz": "America/Los_Angeles"
    },
    {
      "activity_periods": [
        {
          "end_time": "Mar 28 2020 07:18pm",
          "start_time": "Mar 28 2020 06:48pm"
        },
        {
          "end_time": "Mar 28 2020 07:48pm",
          "start_time": "Mar 28 2020 07:18pm"
        },
        {
          "end_time": "Mar 28 2020 08:18pm",
          "start_time": "Mar 28 2020 07:48pm"
        }
      ],
      "id": 2,
      "real_name": "Glinda Southgood",
      "tz": "Asia/Kolkata"
    }
  ],
  "ok": true
}
