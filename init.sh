python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
npm install react react-dom
npm install --save-dev @babel/core
npm install --save-dev @babel/preset-env @babel/preset-react
npm install --save-dev webpack webpack-cli webpack-bundle-tracker babel-loader css-loader style-loader clean-webpack-plugin