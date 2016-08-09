FactoryGirl.define do
  factory :file_position do
    semantic_event
    sequence(:commit_hash) { |n| "commithash#{n}"}
    sequence(:filename) { |n| "filename_#{n}"}
    sequence(:line_number)
  end
end
