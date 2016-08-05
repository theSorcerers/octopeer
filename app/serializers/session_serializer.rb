class SessionSerializer < ActiveModel::Serializer
  attributes :id
  has_one :pull_request
  has_one :user
end
