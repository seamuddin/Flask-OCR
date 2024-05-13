import re

data = """
001. নাম: মোঃ আঙ্গুর ভুইয়া 002. নাম: শ্রী চঞ্চল চন্দ্র শীল ভোটার নং: 680019036102 ভোটার নং: 680019036104 পিতা: মজ্লু ভূইয়া পিতা: শ্রী জিতেন্দ্র শীল মাতা: ফরিদা বেগম মাতা: সন্ধ্যা রানী শিল্‌ কা পেশা: কৃষক,জন্ম তারিখ:০১/০৩/১৯৫৮ পেশা: কৃষ্ক,জন্ম তারিখ:১৬/০৫/১৯৬০ কর্তন করা হয়েছে ঠিকানা: দক্ষিন ধুরু, বেলাবো, নরসিংদী ঠিকানা: শ্রী চঞ্চল চন্দ্র শীলের বাড়ী, দক্ষিন ধুরু, দক্ষিণ ধুরু, বেলাবো, নরসিংদী 004. নাম: মোঃ গিয়াস উদ্দিন ভুইয়া 005. নাম: মোঃ আওলাদ হোসেন ভুইয়া 006. নাম: মোঃ সোহরাব হোসেন ভুইয়া ভোটার নং: 6880019036112 ভোটার নং: 680019036120 ভোটার নং: 680019036122 পিতা: মোঃ মোমতাজ উদ্দিন ভূইয়া পিতা: মোঃ রাজি উদ্দিন ভূইয়া পিতা: মোঃ হাছেন আলী ভূইয়া মাতা: বাতাসী বেগম মাতা: মিসেস রহিমা আক্তার মাতা: মোসাঃ ছোফিয়া খাতুন পেশা: বেকার,জন্ম তারিখ:২০/০২/১৯৫২ পেশা: বেকার,জন্ম তারিখ:০৮/১২/১৯৮২ পেশা: ব্যবসা,জন্ম তারিখ:১০/১২/১৯৮১ ঠিকানা: মোঃ গিয়াস উদ্দিনের বাড়ি, দক্ষিণ ধুরু, বেলাবো, নরসিংদী ঠিকানা মো আওলাদ হুসেনর বাড়ি, দক্ষিণ ধুরু, বেলাবো, ঠিকানা: মোঃ হাছেন আলীর বাড়ি, দক্ষিণ ধুরু, বেলাবো, নরসিংদী রসিং 007. নাম: আবদুল মজিদ 008. নাম: মোঃ মাসুদ ভূইয়া 009. নাম: মোঃ জয়নাল আবেদীন ভূইয়া ভোটার নং: 680019036127 ভোটার নং: 680019036124 ভোটার নং: 680019036127 পিতা: মোঃ হাছেন উদ্দিন ভূইয়া পিতা: মোঃ আঃ ছাত্তার ভূইয়া পিতা: মোঃ মালেক ভূইয়া মাতা: মিসেস সুফিয়া খাতুন মাতা: সমুজা বেগম মাতা: জোবেদা বেগম পেশা: ব্যবসা,জন্ম তারিখ:২৮/০৫/১৯৭৬ পেশা: বেকার,জন্ম তারিখ:০২/০২/১৯৮৯ পেশা: কৃষ্ক,জন্ম তারিখ:১৪/০২/১৯৬৩ ঠিকানা: আবদুল মজিদের বাড়ি, দক্ষিণ ধুরু, বেলাবো, নরসিংদী ঠিকানা: ভূঁইয়া বাড়ী, দক্ষিণ ধুরু, দক্ষিণ ধূরু, বেলাবো, নরসিংদী |
"""

# Define regex patterns
sl_no_pattern = r'\d{3}\.'
name_pattern = r'নাম:\s*(.*?)\s'
voter_no_pattern = r'ভোটার\sনং:\s*(\d+)\s'
father_pattern = r'পিতা:\s*(.*?)\s'
mother_pattern = r'মাতা:\s*(.*?)\s'
occupation_pattern = r'পেশা:\s*(.*?)\s'
address_pattern = r'ঠিকানা:\s*(.*?)\s'
dob_pattern = r'জন্ম\sতারিখ:\s*([\d/]+)\s'

# Compile regex patterns
sl_no_regex = re.compile(sl_no_pattern)
name_regex = re.compile(name_pattern)
voter_no_regex = re.compile(voter_no_pattern)
father_regex = re.compile(father_pattern)
mother_regex = re.compile(mother_pattern)
occupation_regex = re.compile(occupation_pattern)
address_regex = re.compile(address_pattern)
dob_regex = re.compile(dob_pattern)

# Extract information
sl_nos = sl_no_regex.findall(data)
names = name_regex.findall(data)
voter_nos = voter_no_regex.findall(data)
fathers = father_regex.findall(data)
mothers = mother_regex.findall(data)
occupations = occupation_regex.findall(data)
addresses = address_regex.findall(data)
dobs = dob_regex.findall(data)

# Printing extracted information
for sl_no, name, voter_no, father, mother, occupation, address, dob in zip(sl_nos, names, voter_nos, fathers, mothers, occupations, addresses, dobs):
    print("SL No:", sl_no.strip())
    print("নাম:", name.strip())
    print("ভোটার নং:", voter_no.strip())
    print("পিতা:", father.strip())
    print("মাতা:", mother.strip())
    print("পেশা:", occupation.strip())
    print("ঠিকানা:", address.strip())
    print("জন্ম তারিখ:", dob.strip())
    print()