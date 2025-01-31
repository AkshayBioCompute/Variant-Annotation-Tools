function clinvar_sig(clnsig)
    if clnsig == "0" then
        return "Uncertain significance"
    elseif clnsig == "1" then
        return "Not provided"
    elseif clnsig == "2" then
        return "Benign"
    elseif clnsig == "3" then
        return "Likely benign"
    elseif clnsig == "4" then
        return "Likely pathogenic"
    elseif clnsig == "5" then
        return "Pathogenic"
    elseif clnsig == "6" then
        return "Drug response"
    elseif clnsig == "7" then
        return "Histocompatibility"
    elseif clnsig == "255" then
        return "Other"
    else
        return "Unknown"
    end
end

