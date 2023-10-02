def clean_text(text):
      """
      Clean the text of data
      """
      punctuation_list  = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
      acceptable_list = "?\"\'().,!%"
      remove_list = list(filter(lambda punctuation_list: punctuation_list[0] not in acceptable_list, punctuation_list))
      remove_list.append('•')

      text = text.replace('\n', ' ')
      has_any_remove = any([char in remove_list for char in text])
      if has_any_remove:
          for r in remove_list:
              if r in text:
                  text = text.replace(r, ' ')
      has_any_accept = any([char in acceptable_list for char in text])
      if has_any_accept:
          for a in acceptable_list:
              if a in text and a not in "\"\'":
                  text = re.sub(re.escape(a) + r"{2,}", a,text)
                  text = text.replace(a, a+' ')
      text = re.sub(r' {2,}', ' ',text)
      text = text.strip()
      return text
