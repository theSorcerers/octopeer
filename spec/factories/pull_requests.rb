FactoryGirl.define do
  factory :pull_request do
    repository
    sequence(:pull_request_number)
  end
end
