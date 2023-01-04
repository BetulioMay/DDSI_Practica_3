#!/usr/bin/env pwsh

compress-archive -path ".\src",".\db",".\docs\informe.pdf",".\requirements.txt",".\run.ps1",".\.envrc" ".\entrega.zip" -compressionlevel optimal -Force