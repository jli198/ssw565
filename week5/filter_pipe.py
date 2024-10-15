import string

# Filter 1: Remove punctuation
def remove_punctuation(text):
  return text.translate(str.maketrans('', '', string.punctuation))

# Filter 2: Convert to lowercase
def to_lowercase(text):
  return text.lower()

# Filter 3: Remove stop words
def remove_stop_words(text, stop_words):
  return ' '.join([word for word in text.split() if word not in stop_words])

# Main pipe-filter function
def process_text_pipeline(text):
	# please add your code
  stop_words = ["the", "is", "a", "an", "and", "but", "or", "in", "on", "at", "with", "he", "she", "it", "they", "is", "am", "are", "was", "were", "be", "being", "been", "of", "into", "which"]
  remove_punctuation_text = remove_punctuation(text)
  to_lowercase_text = to_lowercase(remove_punctuation_text)
  text = remove_stop_words(to_lowercase_text, stop_words) 
  return text

# Test the pipeline
if __name__ == "__main__":    
  input_text = input("Enter some text: ")
  processed_text = process_text_pipeline(input_text)
  print("Processed text:", processed_text)