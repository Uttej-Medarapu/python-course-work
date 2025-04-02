chat_data = [
    "Alice: Hey Bob, how’s your day going? 😊",
    "Bob: Hey Alice! Pretty good. Just finishing some work. What about you?",
    "Charlie: Hello everyone! Hope you all are doing great.",
    "Alice: I’m doing well too. By the way, are we meeting tomorrow?",
    "Bob: Yeah, I’m free. What’s the plan?",
    "Charlie: Let’s meet at the café around 5 PM.",
    "Alice: Sounds good!",
    "David: Hey, I just joined. What’s up?",
    "Bob: We are planning to meet tomorrow at the café. Wanna join?",
    "David: Yeah, I’d love to!",
    "Alice: Awesome! See you all there.",
    "Charlie: Great! See you tomorrow.",
    "Bob: Sure!"
]
#1.total messages in this chat
print(len(chat_data))
print(type(chat_data))
#2.unique users in this chat
u_users=set()
for message in chat_data:
    user = message.split(":")[0]
    u_users.add(user)
print(u_users)

# 3. Count the Total Words
k=0
for message in chat_data:
    Words=len(message.split(" "))
    k += (Words)
print(f"no of words are:{k}")

#4.average words per message
avg_words=k/len(chat_data)
print(f"Average words per message: {avg_words:.2f}")

#5.Identifying Longest message  
longest_message = ""
length = 0
for message in chat_data:
    if len(message.split()) > length:
        length = len(message.split())
        longest_message = message
print(f"Longest message:{longest_message}")

# 6. most active user sent

user_message_count = {}
for message in chat_data:
    user = message.split(":")[0]
    user_message_count[user] = user_message_count.get(user, 0) + 1
most_active_user = max(user_message_count, key=user_message_count.get)
print(f"Most active user: {most_active_user}")

#7.message count for a specific user
specific_user = input("Enter a user to find message count: ")
print(f"{specific_user} sent {user_message_count.get(specific_user, 0)} messages.")

# 8. Find the Most Frequently Used Word by a User
specific_user = input("Enter a user to find their most frequently used word: ")
word_count = {}

for message in chat_data:
    if message.startswith(specific_user + ":"):
        words = message.split(":")[1].strip().split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

if word_count:
    most_used_word = max(word_count, key=word_count.get)
    print(f"Most frequently used word by {specific_user}: {most_used_word}")
else:
    print(f"No messages found for {specific_user}")


# 9. Retrieve the First and Last Message Sent by a User
user_name = input("Enter a user name to find first and last message: ")
user_messages = []
for message in chat_data:
     if message.startswith(user_name + ":"):
        user_messages.append(message)
if len(user_messages) > 0:
    print(f"First message is: {user_messages[0]}")
    print(f"Last message is: {user_messages[-1]}")

# 10.Check if a User is Present in the Chat
user_present=input("Enter user name:")
if user_present in u_users:
     print(f"{user_present} is present in the chat.")
else:
    print(f"{user_present} is not in the chat.")

# 11. Find Commonly Repeated Words
word_occurrences = {}

for message in chat_data:
    words = message.split(":")[1].strip().split()
    for word in words:
        word_occurrences[word] = word_occurrences.get(word, 0) + 1

common_words = [word for word, count in word_occurrences.items() if count > 1]
print("Commonly repeated words:", common_words)

# 12. Find Messages Containing a Specific Keyword
keyword = input("Enter a keyword to search in messages: ").lower()
for message in chat_data:
    if keyword in message.lower():
        print("Message containing", keyword, "in this", message)

# 13. Identify the User with the Longest Average Message Length
user_word_counts = {}
user_message_counts = {}

for message in chat_data:
    user, text = message.split(":", 1)
    word_count = len(text.strip().split())
    
    user_word_counts[user] = user_word_counts.get(user, 0) + word_count
    user_message_counts[user] = user_message_counts.get(user, 0) + 1

longest_avg_user = max(user_word_counts, key=lambda user: user_word_counts[user] / user_message_counts[user])
print(f"User with the longest average message length: {longest_avg_user}")


# 14. Count How Many Messages Mention a Specific User
mention_user = input("Enter a name to count mentions: ")  
mention_count = 0 

for message in chat_data:
    if mention_user in message:  
        mention_count += 1

print(f"{mention_user} was mentioned in {mention_count} messages.")


# 15. Display the First and Last Message in the Chat
print(f"First message in chat: {chat_data[0]}")
print(f"Last message in chat: {chat_data[-1]}")

# 16. Remove Duplicate Messages
unique_messages = set(chat_data)
print("Unique messages:", unique_messages)

# 17. Find Commonly Used Phrases
phrase_count = {}

for message in chat_data:
    words = message.split(":")[1].strip().split()
    for i in range(len(words) - 1):  # Considering two-word phrases
        phrase = words[i] + " " + words[i + 1]
        phrase_count[phrase] = phrase_count.get(phrase, 0) + 1

common_phrases = [phrase for phrase, count in phrase_count.items() if count > 1]
print("Commonly used phrases:", common_phrases)


# 18. Sort Messages Alphabetically
print("Msgs in alphabetical order:", sorted(chat_data))

# 19. Display Messages in Reverse Order
print("Msgs in reverse order:", chat_data[::-1])

# 20. Find Messages Containing Emojis
emoji = input("Enter a emoji to search in messages(like 😊 ): ")
for message in chat_data:
    if emoji in message:
        print("this emoji ", emoji, "in this", message)

# 21. Find the Most Frequently Used Word in the Chat
word_counts = {}
for message in chat_data:
    words = message.split(":")[1].strip().split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
if word_counts:
    most_frequent_word = max(word_counts, key=word_counts.get)
    print(f"Most frequently used word in chat: {most_frequent_word}")




# 22. Extract All Questions Asked in the Chat
questions = [message for message in chat_data if "?" in message]
print("Questions asked in the chat:")
for q in questions:
    print(q)

# 23. Calculate the Reply Ratio Between Two Users
user1 = input("Enter first user: ")
user2 = input("Enter second user: ")

user1_replies = 0
user2_replies = 0

for i in range(len(chat_data) - 1):
    current_user = chat_data[i].split(":")[0]
    next_user = chat_data[i + 1].split(":")[0]
    if current_user == user1 and next_user == user2:
        user2_replies += 1
    elif current_user == user2 and next_user == user1:
        user1_replies += 1
if user2_replies + user1_replies > 0:
    ratio = user1_replies / (user2_replies + user1_replies)
    print(f"Reply ratio of {user1} to {user2}: {ratio:.2f}")


# 24. Check for Deleted Messages
deleted_messages = [message for message in chat_data if "this message was deleted" in message.lower()]

if deleted_messages:
    print(f"Deleted messages found: {len(deleted_messages)}")


#25.Messages Sent After a Specific Keyword
word = input("Enter a keyword to find messages sent after it: ").lower()
index = -1  
for i in range(len(chat_data)):
    if word in chat_data[i].lower(): 
        index = i
if index != -1 and index + 1 < len(chat_data):  
    print("Message sent after the given word:", chat_data[index + 1])


