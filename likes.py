def max_engagement(views, likes):
    # Step 1: Find the maximum element in views and likes
    max_view = max(views)
    max_like = max(likes)
    
    # Step 2: Find their corresponding indices
    max_view_index = views.index(max_view)
    max_like_index = likes.index(max_like)
    
    # Step 3: Compare max elements
    engagement_score = 0
    final_likes_arrangement = [0] * len(views)
    
    if max_view > max_like:
        # If the maximum view is greater than the maximum like
        print("Maximum view is greater than maximum like, engagement score will be zero.")
    else:
        # Step 4: Rearranging likes to maximize engagement score
        sorted_likes = sorted(likes, reverse=True)
        
        like_index = 0  # Pointer for sorted_likes
        
        for i in range(len(views)):
            # Try to find a like that is greater than the current view
            while like_index < len(sorted_likes) and sorted_likes[like_index] <= views[i]:
                like_index += 1
                
            # If a suitable like is found
            if like_index < len(sorted_likes):
                engagement_score += sorted_likes[like_index]  # Add to score
                final_likes_arrangement[i] = sorted_likes[like_index]  # Assign to the final arrangement
                like_index += 1  # Move to the next like
    
        # Fill remaining likes in the final arrangement
        for j in range(len(final_likes_arrangement)):
            if final_likes_arrangement[j] == 0 and like_index < len(sorted_likes):
                final_likes_arrangement[j] = sorted_likes[like_index]
                like_index += 1

    # Step 5: Print the final arrangement of likes and the engagement score
    print("Rearranged likes for maximum engagement:", final_likes_arrangement)
    return engagement_score

# Example test case
views = [10, 2, 4, 11]
likes = [5, 2, 9, 2]

# Calculate the maximum engagement score
max_score = max_engagement(views, likes)
print("Maximum Engagement Score:", max_score)
