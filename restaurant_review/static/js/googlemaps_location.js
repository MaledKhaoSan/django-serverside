let map;
let marker;

function initMap() {
    const initialLocation = { lat: 13.736717, lng: 100.523186 }; // Bangkok

    map = new google.maps.Map(document.getElementById('map'), {
        center: initialLocation,
        zoom: 12,
    });

    marker = new google.maps.Marker({
        map: map,
        position: initialLocation,
        draggable: true,
    });

    // Event listener สำหรับการลากหมุด (marker) เสร็จสิ้น
    marker.addListener('dragend', function () {
        const newPosition = marker.getPosition(); // รับตำแหน่งใหม่ของหมุด
        const userLocation = {
            lat: newPosition.lat(),
            lng: newPosition.lng()
        };

        // อัปเดต latitude และ longitude ในฟอร์ม
        document.getElementById('id_latitude').value = userLocation.lat;
        document.getElementById('id_longitude').value = userLocation.lng;

        // ใช้ reverse geocoding เพื่อดึงข้อมูลจังหวัด, อำเภอ, ตำบลจากตำแหน่งใหม่
        geocodeLatLng(userLocation);
    });
    
    // Event listener สำหรับปุ่ม "ใช้ตำแหน่งของฉัน"
    document.getElementById('find-location-btn').addEventListener('click', function(e) {
        e.preventDefault();
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };

                // ปรับแผนที่และ marker ไปยังตำแหน่งผู้ใช้
                map.setCenter(userLocation);
                map.setZoom(15);
                marker.setPosition(userLocation);

                // อัปเดต latitude และ longitude
                document.getElementById('id_latitude').value = userLocation.lat;
                document.getElementById('id_longitude').value = userLocation.lng;

                // Reverse Geocoding เพื่อดึงข้อมูลจังหวัด, อำเภอ, ตำบล
                geocodeLatLng(userLocation);
            });
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    });
}

// ฟังก์ชันเพื่อดึงข้อมูลที่อยู่จาก LatLng
function geocodeLatLng(location) {
    const geocoder = new google.maps.Geocoder();
    geocoder.geocode({ location: location }, function(results, status) {
        if (status === "OK") {
            if (results[0]) {
                const components = results[0].address_components;
                let province = "";
                let district = "";
                let subdistrict = "";

                components.forEach(function(component) {
                    if (component.types.includes("administrative_area_level_1")) {
                        province = component.long_name;
                    } else if (component.types.includes("administrative_area_level_2")) {
                        district = component.long_name;
                    } else if (component.types.includes("sublocality_level_1") || component.types.includes("administrative_area_level_3")) {
                        subdistrict = component.long_name;
                    }
                });

                // กรณีไม่มีค่า district หรือ subdistrict ให้ใช้ค่าที่มีอยู่แทนกัน
                if (!district && subdistrict) {
                    district = subdistrict;
                } else if (!subdistrict && district) {
                    subdistrict = district;
                }

                console.log(province)
                console.log(district)
                console.log(subdistrict)
                // บันทึกข้อมูลลงใน hidden fields
                document.getElementById('id_province').value = province;
                document.getElementById('id_district').value = district;
                document.getElementById('id_subdistrict').value = subdistrict;

                // บันทึกข้อมูลลงใน dropdown
                document.getElementById('provinceDropdown').innerHTML = `<option value="${province}">${province}</option>`;
                document.getElementById('districtDropdown').innerHTML = `<option value="${district}">${district}</option>`;
                document.getElementById('subdistrictDropdown').innerHTML = `<option value="${subdistrict}">${subdistrict}</option>`;
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', initMap);
