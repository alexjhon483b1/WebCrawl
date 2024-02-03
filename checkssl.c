#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    return size * nmemb;
}

int checkProtocol(const char* url, long timeout) {
    CURL* curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_NOBODY, 1L); // Only fetch the headers, not the body
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L); // Follow redirects
        curl_easy_setopt(curl, CURLOPT_TIMEOUT, timeout); // Set timeout in seconds

        res = curl_easy_perform(curl);

        if (res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
            curl_easy_cleanup(curl);
            curl_global_cleanup();
            return -1;
        }

        long response_code;
        curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &response_code);

        if (response_code == 200) {
            printf("HTTPS\n");
        } else if (response_code == 301 || response_code == 302) {
            printf("HTTPS\n");
        } else {
            printf("HTTP\n");
        }

        curl_easy_cleanup(curl);
    }

    curl_global_cleanup();
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <domain> <timeout>\n", argv[0]);
        return 1;
    }

    const char* url = argv[1];
    long timeout = strtol(argv[2], NULL, 10);
    
    if (timeout <= 0) {
        fprintf(stderr, "Timeout must be a positive integer.\n");
        return 1;
    }

    checkProtocol(url, timeout);

    return 0;
}

