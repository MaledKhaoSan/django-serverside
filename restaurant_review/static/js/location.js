//restaurant_review/static/js/location.js

const toggleButton = document.getElementById("toggle-location");
const dropdownSection = document.getElementById("dropdown-location");
const mapSection = document.getElementById("googlemaps-picker-location");
const provinceDropdown = document.getElementById("provinceDropdown");
const districtDropdown = document.getElementById("districtDropdown");
const subdistrictDropdown = document.getElementById("subdistrictDropdown");
const provinceInput = document.getElementById("id_province");
const districtInput = document.getElementById("id_district");
const subdistrictInput = document.getElementById("id_subdistrict");
const latitudeInput = document.getElementById("id_latitude");
const longitudeInput = document.getElementById("id_longitude");
let usingGoogleMaps = false;

document.addEventListener('DOMContentLoaded', function() {
    loadProvinceData(); // Load provinces on page load
});

// Add event listener to load districts when a province is selected
provinceDropdown.addEventListener('change', function() {
    const provinceId = this.value;
    if (provinceId) {
        loadDistrictData(provinceId);  // Call to load districts
        provinceInput.value = provinceDropdown.options[provinceDropdown.selectedIndex].text; // Update hidden province input
    }
});

districtDropdown.addEventListener("change", function () {
    const districtId = districtDropdown.value;
    if (districtId) {
        loadSubdistrictData(districtId);
        districtInput.value = districtDropdown.options[districtDropdown.selectedIndex].text; // Update hidden district input
    } else {
        subdistrictDropdown.innerHTML = '<option value="">เลือกตำบล</option>';
    }
});

subdistrictDropdown.addEventListener("change", function () {
    if (subdistrictDropdown.value) {
        subdistrictInput.value = subdistrictDropdown.options[subdistrictDropdown.selectedIndex].text; // Update hidden subdistrict input
    }
});

// Toggle between dropdown and Google Maps
toggleButton.addEventListener("click", function () {
    usingGoogleMaps = !usingGoogleMaps;
    if (usingGoogleMaps) {
        dropdownSection.style.display = "none";
        mapSection.style.display = "block";
        toggleButton.textContent = "ใช้ Dropdown";
    } else {
        dropdownSection.style.display = "block";
        mapSection.style.display = "none";
        toggleButton.textContent = "ใช้ Google Maps";
    }
});

// Load province, district, and subdistrict data
function loadProvinceData() {
    fetch("/api/json/provinces/")
        .then(response => response.json())
        .then(provinces => {
            provinces.forEach(province => {
                let option = new Option(province.name_th, province.id);
                provinceDropdown.add(option);
            });
        })
        .catch(error => console.error('Error loading provinces:', error));
}

function loadDistrictData(provinceId) {
    districtDropdown.innerHTML = '<option value="">เลือกเขต/อำเภอ</option>'; // Clear previous options
    fetch(`/api/json/amphures/?province=${provinceId}`)
        .then(response => response.json())
        .then(districts => {
            districts.forEach(district => {
                let option = new Option(district.name_th, district.id);
                districtDropdown.add(option);
            });
        });
}

function loadSubdistrictData(districtId) {
    fetch(`/api/json/tambons/?district=${districtId}`)
        .then(response => response.json())
        .then(subdistricts => {
            subdistrictDropdown.innerHTML = '<option value="">เลือกตำบล</option>';
            subdistricts.forEach(subdistrict => {
                let option = new Option(subdistrict.name_th, subdistrict.id);
                subdistrictDropdown.add(option);
            });
        });
}
