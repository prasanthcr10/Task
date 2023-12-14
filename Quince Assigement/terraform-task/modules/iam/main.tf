resource "aws_iam_user" "newuser" {
    name = var.username
}


resource "aws_iam_access_key" "newuser" {
  user    = aws_iam_user.newuser.name
  
}


resource "aws_iam_user_policy" "newuser_ro" {
  name   = "newuser_ro_policy"
  user   = aws_iam_user.newuser.name
  policy = data.aws_iam_policy_document.newuser_ro.json
}