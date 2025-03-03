package main

import (
	"crypto/sha1"
	"fmt"
	"sort"
	"strings"
)

type PicpikSigner struct {
	publicKey  string
	privateKey string
	apiKey     string
}

func NewPicpikSigner(publicKey, privateKey, apiKey string) *PicpikSigner {
	return &PicpikSigner{
		publicKey:  publicKey,
		privateKey: privateKey,
		apiKey:     apiKey,
	}
}

func (ps *PicpikSigner) mapToString(params map[string]interface{}, exclusiveKey *string, strLimit int) string {
	var content []string
	keys := ps.extractSortedKeys(params)
	for _, key := range keys {
		if exclusiveKey == nil || len(*exclusiveKey) == 0 || *exclusiveKey != key {
			content = append(content, key+ps.anyToString(params[key], strLimit))
		}
	}
	return strings.Join(content, "")
}

func (ps *PicpikSigner) anyToString(v interface{}, strLimit int) string {
	switch v := v.(type) {
	case bool:
		return strings.ToLower(ps.simpleToString(v))
	case float64:
		if float64(int(v)) == v {
			return ps.simpleToString(int(v))
		}
		return ps.simpleToString(v)
	case map[string]interface{}:
		return ps.mapToString(v, nil, strLimit)
	case []interface{}:
		return ps.sliceToString(v, strLimit)
	case string:
		return ps.formatString(v, strLimit)
	default:
		return ps.simpleToString(v)
	}
}

func (ps *PicpikSigner) sliceToString(arr []interface{}, strLimit int) string {
	var result string
	for _, v := range arr {
		result += ps.anyToString(v, strLimit)
	}
	return result
}

func (ps *PicpikSigner) simpleToString(v interface{}) string {
	if v == nil || v == "" {
		return ""
	}
	return fmt.Sprintf("%v", v)
}

func (ps *PicpikSigner) formatString(v string, limit int) string {
	if limit > 0 && len(v) > limit {
		return v[:limit]
	}
	return v
}

func (ps *PicpikSigner) extractSortedKeys(obj map[string]interface{}) []string {
	keys := make([]string, 0, len(obj))
	for key := range obj {
		keys = append(keys, key)
	}
	sort.Strings(keys)
	return keys
}

func (ps *PicpikSigner) SignService(body map[string]interface{}) string {
	content := ps.mapToString(body, nil, 128) + ps.apiKey
	sha1Hash := sha1.New()
	sha1Hash.Write([]byte(content))
	return fmt.Sprintf("%x", sha1Hash.Sum(nil))
}

func (ps *PicpikSigner) SignPlatform(body map[string]interface{}) string {
	content := ps.mapToString(body, nil, -1) + ps.privateKey
	sha1Hash := sha1.New()
	sha1Hash.Write([]byte(content))
	return fmt.Sprintf("%x", sha1Hash.Sum(nil))
}
