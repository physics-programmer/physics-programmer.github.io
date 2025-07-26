// Physics-Programmer Portfolio Theme JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initMobileMenu();
    initSmoothScrolling();
    initCodeBlocks();
    initSearchFunctionality();
    initThemeToggle();
    initPerformanceMonitoring();
    initAccessibilityEnhancements();
});

/**
 * Mobile Navigation Menu
 */
function initMobileMenu() {
    const toggleButton = document.querySelector('.navbar-toggle');
    const mobileMenu = document.querySelector('.navbar-menu');
    
    if (!toggleButton || !mobileMenu) return;
    
    toggleButton.addEventListener('click', function() {
        const isExpanded = toggleButton.getAttribute('aria-expanded') === 'true';
        
        // Toggle visibility
        mobileMenu.style.display = isExpanded ? 'none' : 'block';
        
        // Update accessibility attributes
        toggleButton.setAttribute('aria-expanded', !isExpanded);
        
        // Animate hamburger lines
        const lines = toggleButton.querySelectorAll('.hamburger-line');
        if (!isExpanded) {
            lines[0].style.transform = 'rotate(-45deg) translate(-5px, 6px)';
            lines[1].style.opacity = '0';
            lines[2].style.transform = 'rotate(45deg) translate(-5px, -6px)';
        } else {
            lines.forEach(line => {
                line.style.transform = '';
                line.style.opacity = '';
            });
        }
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!toggleButton.contains(event.target) && !mobileMenu.contains(event.target)) {
            mobileMenu.style.display = 'none';
            toggleButton.setAttribute('aria-expanded', 'false');
            
            // Reset hamburger lines
            const lines = toggleButton.querySelectorAll('.hamburger-line');
            lines.forEach(line => {
                line.style.transform = '';
                line.style.opacity = '';
            });
        }
    });
    
    // Close menu on escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && mobileMenu.style.display === 'block') {
            mobileMenu.style.display = 'none';
            toggleButton.setAttribute('aria-expanded', 'false');
            toggleButton.focus();
        }
    });
}

/**
 * Smooth Scrolling for Anchor Links
 */
function initSmoothScrolling() {
    const anchors = document.querySelectorAll('a[href^="#"]');
    
    anchors.forEach(anchor => {
        anchor.addEventListener('click', function(event) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (!target) return;
            
            event.preventDefault();
            
            // Calculate offset for fixed header
            const headerOffset = 80;
            const elementPosition = target.offsetTop;
            const offsetPosition = elementPosition - headerOffset;
            
            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
            
            // Update URL without triggering scroll
            history.pushState(null, null, href);
            
            // Focus target for accessibility
            target.focus();
        });
    });
}

/**
 * Code Block Enhancements
 */
function initCodeBlocks() {
    const codeBlocks = document.querySelectorAll('.highlight');
    
    codeBlocks.forEach(block => {
        // Add copy functionality
        addCopyButton(block);
        
        // Add language label
        addLanguageLabel(block);
        
        // Add line numbers if needed
        addLineNumbers(block);
    });
}

function addCopyButton(codeBlock) {
    const button = document.createElement('button');
    button.className = 'copy-button';
    button.textContent = 'Copy';
    button.setAttribute('aria-label', 'Copy code to clipboard');
    
    button.addEventListener('click', async function() {
        const code = codeBlock.querySelector('code');
        if (!code) return;
        
        try {
            await navigator.clipboard.writeText(code.textContent);
            
            // Visual feedback
            button.textContent = 'Copied!';
            button.classList.add('copied');
            
            setTimeout(() => {
                button.textContent = 'Copy';
                button.classList.remove('copied');
            }, 2000);
            
        } catch (err) {
            console.error('Failed to copy code:', err);
            
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = code.textContent;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            
            button.textContent = 'Copied!';
            setTimeout(() => button.textContent = 'Copy', 2000);
        }
    });
    
    codeBlock.style.position = 'relative';
    codeBlock.appendChild(button);
}

function addLanguageLabel(codeBlock) {
    // Extract language from class name (e.g., 'language-python')
    const pre = codeBlock.querySelector('pre');
    if (!pre) return;
    
    const classes = pre.className.split(' ');
    const langClass = classes.find(cls => cls.startsWith('language-'));
    
    if (langClass) {
        const language = langClass.replace('language-', '');
        codeBlock.setAttribute('data-lang', language);
    }
}

function addLineNumbers(codeBlock) {
    const pre = codeBlock.querySelector('pre');
    if (!pre || pre.querySelector('.linenos')) return;
    
    const code = pre.querySelector('code');
    if (!code) return;
    
    const lines = code.textContent.split('\n');
    if (lines.length < 5) return; // Only add line numbers for longer code blocks
    
    const lineNumbers = lines.map((_, index) => index + 1).join('\n');
    
    const table = document.createElement('table');
    table.innerHTML = `
        <tr>
            <td class="linenos"><pre>${lineNumbers}</pre></td>
            <td class="code">${pre.outerHTML}</td>
        </tr>
    `;
    
    codeBlock.innerHTML = '';
    codeBlock.appendChild(table);
}

/**
 * Search Functionality
 */
function initSearchFunctionality() {
    const searchInput = document.querySelector('.search-input');
    const searchResults = document.querySelector('.search-results');
    
    if (!searchInput) return;
    
    let searchIndex = [];
    let searchTimeout;
    
    // Build search index from page content
    buildSearchIndex();
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            performSearch(this.value.trim());
        }, 300);
    });
    
    function buildSearchIndex() {
        const articles = document.querySelectorAll('article');
        
        articles.forEach(article => {
            const title = article.querySelector('h1, h2, h3')?.textContent || '';
            const content = article.textContent || '';
            const url = article.querySelector('a')?.href || '';
            
            searchIndex.push({
                title,
                content: content.toLowerCase(),
                url,
                element: article
            });
        });
    }
    
    function performSearch(query) {
        if (!query || query.length < 2) {
            hideSearchResults();
            return;
        }
        
        const results = searchIndex.filter(item => 
            item.title.toLowerCase().includes(query.toLowerCase()) ||
            item.content.includes(query.toLowerCase())
        );
        
        displaySearchResults(results, query);
    }
    
    function displaySearchResults(results, query) {
        if (!searchResults) return;
        
        if (results.length === 0) {
            searchResults.innerHTML = '<div class="no-results">No results found</div>';
        } else {
            const html = results.slice(0, 5).map(result => `
                <div class="search-result">
                    <h4><a href="${result.url}">${result.title}</a></h4>
                    <p>${getExcerpt(result.content, query)}</p>
                </div>
            `).join('');
            
            searchResults.innerHTML = html;
        }
        
        searchResults.style.display = 'block';
    }
    
    function getExcerpt(content, query) {
        const index = content.toLowerCase().indexOf(query.toLowerCase());
        const start = Math.max(0, index - 50);
        const end = Math.min(content.length, index + query.length + 50);
        
        let excerpt = content.slice(start, end);
        if (start > 0) excerpt = '...' + excerpt;
        if (end < content.length) excerpt += '...';
        
        return excerpt.replace(
            new RegExp(query, 'gi'), 
            match => `<mark>${match}</mark>`
        );
    }
    
    function hideSearchResults() {
        if (searchResults) {
            searchResults.style.display = 'none';
        }
    }
    
    // Close search results when clicking outside
    document.addEventListener('click', function(event) {
        if (!searchInput.contains(event.target) && 
            !searchResults?.contains(event.target)) {
            hideSearchResults();
        }
    });
}

/**
 * Theme Toggle (Dark/Light Mode)
 */
function initThemeToggle() {
    const themeToggle = document.querySelector('.theme-toggle');
    if (!themeToggle) return;
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme') || 
                      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    
    setTheme(savedTheme);
    
    themeToggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        setTheme(newTheme);
        localStorage.setItem('theme', newTheme);
    });
    
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        themeToggle.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
    }
    
    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
        if (!localStorage.getItem('theme')) {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });
}

/**
 * Performance Monitoring
 */
function initPerformanceMonitoring() {
    if (!window.performance || !window.performance.timing) return;
    
    window.addEventListener('load', function() {
        setTimeout(() => {
            const timing = performance.timing;
            const loadTime = timing.loadEventEnd - timing.navigationStart;
            const domReady = timing.domContentLoadedEventEnd - timing.navigationStart;
            
            // Log performance metrics
            console.log('Performance Metrics:', {
                loadTime: loadTime + 'ms',
                domReady: domReady + 'ms',
                firstPaint: getFirstPaint(),
                largestContentfulPaint: getLCP()
            });
            
            // Send to analytics if configured
            if (typeof gtag === 'function') {
                gtag('event', 'timing_complete', {
                    name: 'load',
                    value: loadTime
                });
            }
        }, 1000);
    });
}

function getFirstPaint() {
    const paintEntries = performance.getEntriesByType('paint');
    const firstPaint = paintEntries.find(entry => entry.name === 'first-paint');
    return firstPaint ? Math.round(firstPaint.startTime) + 'ms' : 'N/A';
}

function getLCP() {
    if (!window.PerformanceObserver) return 'N/A';
    
    let lcp = 'N/A';
    
    try {
        const observer = new PerformanceObserver((list) => {
            const entries = list.getEntries();
            const lastEntry = entries[entries.length - 1];
            lcp = Math.round(lastEntry.startTime) + 'ms';
        });
        
        observer.observe({ entryTypes: ['largest-contentful-paint'] });
        
        setTimeout(() => observer.disconnect(), 5000);
    } catch (e) {
        console.warn('LCP measurement not supported');
    }
    
    return lcp;
}

/**
 * Accessibility Enhancements
 */
function initAccessibilityEnhancements() {
    // Focus management for skip links
    const skipLink = document.querySelector('.skip-link');
    const mainContent = document.querySelector('#main-content');
    
    if (skipLink && mainContent) {
        skipLink.addEventListener('click', function(e) {
            e.preventDefault();
            mainContent.focus();
        });
    }
    
    // Keyboard navigation for interactive elements
    const interactiveElements = document.querySelectorAll('.project-card, .domain-card, .timeline-item');
    
    interactiveElements.forEach(element => {
        element.setAttribute('tabindex', '0');
        
        element.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                const link = this.querySelector('a');
                if (link) {
                    e.preventDefault();
                    link.click();
                }
            }
        });
    });
    
    // Announce page navigation to screen readers
    announcePageNavigation();
    
    // Improved focus indicators
    addFocusIndicators();
}

function announcePageNavigation() {
    const pageTitle = document.title;
    const announcement = document.createElement('div');
    announcement.setAttribute('aria-live', 'polite');
    announcement.setAttribute('aria-atomic', 'true');
    announcement.className = 'sr-only';
    announcement.textContent = `Navigated to ${pageTitle}`;
    
    document.body.appendChild(announcement);
    
    setTimeout(() => {
        document.body.removeChild(announcement);
    }, 1000);
}

function addFocusIndicators() {
    const style = document.createElement('style');
    style.textContent = `
        .enhanced-focus:focus {
            outline: 3px solid #3498db;
            outline-offset: 2px;
            border-radius: 4px;
        }
        
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }
    `;
    
    document.head.appendChild(style);
    
    // Add enhanced focus class to focusable elements
    const focusableElements = document.querySelectorAll('a, button, input, textarea, select, [tabindex]');
    focusableElements.forEach(element => {
        element.classList.add('enhanced-focus');
    });
}

/**
 * Utility Functions
 */

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function for scroll events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Scroll position tracking
let ticking = false;

function updateScrollPosition() {
    const scrolled = window.pageYOffset;
    const header = document.querySelector('.site-header');
    
    if (header) {
        if (scrolled > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
    
    ticking = false;
}

window.addEventListener('scroll', function() {
    if (!ticking) {
        requestAnimationFrame(updateScrollPosition);
        ticking = true;
    }
});

// Error handling
window.addEventListener('error', function(e) {
    console.error('JavaScript Error:', e.error);
    
    // Send to analytics if configured
    if (typeof gtag === 'function') {
        gtag('event', 'exception', {
            description: e.error.toString(),
            fatal: false
        });
    }
});

// Service Worker registration for PWA capabilities
if ('serviceWorker' in navigator && window.location.protocol === 'https:') {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js').then(function(registration) {
            console.log('ServiceWorker registration successful');
        }).catch(function(err) {
            console.log('ServiceWorker registration failed');
        });
    });
}