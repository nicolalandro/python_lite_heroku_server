# Create a new Heroku app
resource "heroku_app" "default" {
  name = "my-favourite-app-name"
  region = "us"
  stack = "heroku-16"
  buildpacks = [
    "heroku/python"
  ]
  config_vars {
    pcloud_uname = "your_pcloud_email"
    pcloud_password = "your_pcloud_password"
  }
}

# Create a database, and configure the app to use it
#resource "heroku_addon" "database" {
#  app = "${heroku_app.default.name}"
#  plan = "heroku-postgresql:hobby-dev"
#}

#resource "heroku_addon" "newrelic" {
#  app = "${heroku_app.default.name}"
#  plan = "newrelic:stark"
#}

#resource "heroku_addon" "papertrail" {
#  app = "${heroku_app.d#efault.name}"
#  plan = "papertrail"
#}
