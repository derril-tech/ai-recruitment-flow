# Parsers Package Instructions

## Purpose
This package contains document parsers for various file formats used in recruitment.

## Supported Formats
1. **PDF**: Resumes, job descriptions, certificates
2. **DOCX**: Word documents, cover letters
3. **XLSX**: Spreadsheets, candidate lists, reports
4. **CSV**: Data exports, candidate databases
5. **HTML**: Web scraping, LinkedIn profiles

## Development Guidelines
- Support multiple file formats with consistent output
- Implement proper error handling for corrupted files
- Extract structured data (text, tables, metadata)
- Maintain document formatting where relevant
- Include OCR capabilities for scanned documents
- Implement proper file validation and security checks

## Parser Structure
```
src/
  parsers/
    pdf/
      pdf_parser.ts
      pdf_extractor.ts
      pdf_validator.ts
    docx/
      docx_parser.ts
      docx_extractor.ts
      docx_validator.ts
    xlsx/
      xlsx_parser.ts
      xlsx_extractor.ts
      xlsx_validator.ts
    csv/
      csv_parser.ts
      csv_extractor.ts
      csv_validator.ts
    html/
      html_parser.ts
      html_extractor.ts
      html_validator.ts
  types/
    parser_types.ts
    document_types.ts
  utils/
    file_utils.ts
    validation_utils.ts
    ocr_utils.ts
  index.ts
```

## TODO: Implement Parsers
- [ ] PDF Parser (resume extraction, text parsing)
- [ ] DOCX Parser (document processing, formatting preservation)
- [ ] XLSX Parser (spreadsheet data extraction)
- [ ] CSV Parser (data import, validation)
- [ ] HTML Parser (web scraping, profile extraction)

## Parser Capabilities
- **PDF**: Text extraction, table parsing, OCR support
- **DOCX**: Document structure, formatting, metadata
- **XLSX**: Cell data, formulas, charts, multiple sheets
- **CSV**: Delimiter detection, encoding support, validation
- **HTML**: DOM parsing, content extraction, link following

## Testing Requirements
- Unit tests for each parser
- Integration tests with sample documents
- Performance testing for large files
- Error handling tests for corrupted files
