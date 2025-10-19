#台形の面積を求めるプログラム

#上辺の長さ
jouhen=input("上辺の長さは：")
jouhen=float(jouhen)

#下辺の長さ
kahen=input("下辺の長さは：")
kahen=float(kahen)

#高さ
takasa=input("高さは：")
takasa=float(takasa)


#台形の面積
area=(jouhen+kahen)*takasa/2
print(f"台形の面積は{area}です。")
