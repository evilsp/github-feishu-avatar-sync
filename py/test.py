import gitlab

gl=gitlab.Gitlab(url="https://gitlab.redrock.team",private_token="glpat-tGyFCzYXLpFxCG5k9yTL")
a=gl.users.list(iterator=True)
for i in a:
    print(i.asdict()["commit_email"])