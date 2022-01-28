# river = {
#     'Nile':'Egypt',
#     'Dnipro':'Ukraine',
#     'Don':'Russia',
#     }
# for r, c in river.items():
#     print (f"Река {r} протекает через {c}")
# for reka in river.keys():
#     print("\n" + reka.title())
# for country in river.values():
#     print(country.title())
# 6-6
# favorite_languages = {
#     'jen':'python',
#     'edward':'ruby',
#     'phil':'python',
#     'max':'java',
#     'vladimir':'C',
#     'niko':'',
# }
#
# for n,l in favorite_languages.items():
#    if (len(l)>=1):
#     print(f"Спасибо {n.title()} что приняли участие в опросе, вы выбрали"
#           f" {l} верно?")
#    else:
#        print(f"{n.title()} Проголосуйте пожалуйста")


# favorite_languages = {
#         'jen': ['python', 'ruby'],
#         'sarah': ['c'],
#         'edward': ['ruby', 'go'],
#         'phil': ['python', 'haskell'],
#     }
# for name, languages in favorite_languages.items():
#         if len(languages) > 1:
#             substring = " favorite languages are:"
#         else:
#             substring = " favorite language is:"
#         string = name.title() + substring
#         print(string)
#         print(*languages, "\n")