import os

files_to_fix = [
    r'guides\discord-blueprint.html',
    r'guides\general-guide.html',
    r'guides\tiktok-youtube-shorts.html',
    r'guides\angles\scale-safely-with-margins.html',
    r'guides\angles\stop-losing-30-profit.html',
    r'guides\angles\track-profit-like-a-pro.html',
    r'resources\mcp\short-form-video-guidelines.html'
]

for rel_path in files_to_fix:
    path = os.path.join(r'c:\Users\khoadnd\Desktop\onboarding hub', rel_path)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
        
    print(f"Fixing {rel_path}...")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We want to find the first </style>\n</head>\n<body>\nbile for performance */
    # and replace everything up to the next </style>\n</head>\n<body>
    search_str = "</style>\n</head>\n<body>\nbile for performance */"
    # Note that line endings might be \r\n
    if "</style>\n</head>\n<body>\nbile for performance */" not in content:
        # try with \r\n
        search_str = "</style>\r\n</head>\r\n<body>\r\nbile for performance */"
        
    if search_str not in content:
        print(f"Could not find exact signature in {rel_path}")
        continue
        
    start_idx = content.find(search_str)
    
    # Now find the next </style>\n</head>\n<body>
    next_sig = "</style>\n</head>\n<body>"
    next_sig_idx = content.find(next_sig, start_idx + len(search_str))
    if next_sig_idx == -1:
        next_sig = "</style>\r\n</head>\r\n<body>"
        next_sig_idx = content.find(next_sig, start_idx + len(search_str))
        
    if next_sig_idx == -1:
        print(f"Could not find ending signature in {rel_path}")
        continue
        
    # We replace from start_idx to next_sig_idx + len(next_sig) with just next_sig
    new_content = content[:start_idx] + next_sig + content[next_sig_idx + len(next_sig):]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully fixed {rel_path}")
